import util
import index
import conditions

class Query:

    OPERATORS = {"!": "NOT", "&": "AND", "|": "OR"}

    # a base com os nomes do arquivo pode ser passada por parâmetro, ou então o nome do arquivo
    # onde os mesmos estão
    def __init__(self, nomeArqQuery, nomeArqIndice, base={}, nomeArqBase=""):
        self.nomeArqQuery = nomeArqQuery
        self.nomeArqIndice = nomeArqIndice
        self.nomeArqBase = nomeArqBase
        self.base = base
        if nomeArqBase != "":
            arq = open(nomeArqBase, "r")
            i = 1
            for nomeArquivo in arq.read().splitlines():
                self.base[i] = nomeArquivo
                i += 1

    def executeQuery(self):
        query = open(self.nomeArqQuery).read().lower()
        query = util.tokenize(query)
        indObj = index.Index(self.nomeArqBase, self.nomeArqIndice)
        ind = indObj.loadIndex()
        indArqs = self.base.keys()

        #substitui os tokens pelos indices
        for i, v in enumerate(query):
            if v not in self.OPERATORS:
                query[i] = [int(oc.doc) for oc in ind[v]]

        #NOT
        while True:
            flag = False
            for i, v in enumerate(query):
                if v == "!":
                    flag = True
                    del query[i] #remove operator
                    query[i] = conditions.Condition.notCondition(query[i], indArqs)
            
            if not flag:
                break
        
        #AND
        while True:
            flag = False
            for i, v in enumerate(query):
                if v == "&":
                    flag = True
                    del query[i] #remove operator
                    query[i - 1] = conditions.Condition.andCondition(query[i-1], query[i]) #execute intersection
                    del query[i] #remove one of the lists
            
            if not flag:
                break
        
        #OR
        while True:
            flag = False
            for i, v in enumerate(query):
                if (v == "|"):
                    flag = True
                    del query[i] #remove operator
                    query[i - 1] = conditions.Condition.orCondition(query[i-1], query[i]) #execute intersection
                    del query[i] #remove one of the lists
            
            if not flag:
                break

        query[0].sort()
        return [self.base[q] for q in query[0]]

        