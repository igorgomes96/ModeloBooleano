import string
import nltk
import util
import occurrence
from collections import OrderedDict

class Index:
    
    def __init__(self, nomeArqBase, nomeArqIndiceResult):
        self.nomeArqBase = nomeArqBase
        self.nomeArqIndiceResult = nomeArqIndiceResult

    def loadBase(self):
        #abre o arquivo e obtem cada linha do arquivo
        arqBase = open(self.nomeArqBase, 'r')
        arqs = arqBase.read().splitlines()
        dic = {}
        for i in range(0, len(arqs)):
            dic[i+1] = arqs[i]
        
        arqBase.close()
        return dic
    
    def createIndex(self):

        indice = {}
        i = 1

        arquivosTexto = self.loadBase()

        for arquivo in arquivosTexto.values():
            arqTexto = open(arquivo)
            
            #separando as palavras
            tokens = util.tokenize(arqTexto.read().replace(".", " ").replace(",", " ").replace("!", " ").replace("?", " ").replace("\n", " ").lower())
            
            #para cada token
            for token in tokens:
                #se o token já estiver no dictionary
                if token in indice:
                    #se o índíce do arquivo já estiver vinculado ao token
                    if i in indice[token]:
                        indice[token][i] += 1 #incrementa o número de ocorrências
                    else:
                        indice[token][i] = 1 #inicializa com uma ocorrência
                else:
                    indice[token] = {i: 1}  #inicializa o dictionary

            i += 1
            arqTexto.close()

        #ordena o índice
        indice = OrderedDict(sorted(indice.items()))
        #abre o arquivo de índice
        arqIndice = open(self.nomeArqIndiceResult, 'w')

        #para cada token no índice
        for tok, dic in indice.items():
            linha = tok + ":"
            for arq, ocor in dic.items(): #para cada arquivo que contém token
                linha = linha + " " + str(arq) + "," + str(ocor)
            arqIndice.write(linha + "\n")  #grava a linha

        #fecha os arquivos
        arqIndice.close()

    def loadIndex(self):
        arq = open(self.nomeArqIndiceResult)
        index = {}
        for line in arq.read().splitlines():
            splitted = line.split(": ")
            index[splitted[0]] = []
            for d in splitted[1].split(" "):
                v = d.split(",")
                doc = v[0]
                n = v[1]
                occor = occurrence.Occurrence(doc, n)
                index[splitted[0]].append(occor)
        return index

