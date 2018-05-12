import sys
import index
import query

ARQ_INDICE = "result/indice.txt"
ARQ_RESPOSTA = "result/resposta.txt"

# chama a função passando o nome do arquivo base como parâmetro
ind = index.Index(sys.argv[1], ARQ_INDICE)
ind.createIndex()

# chama a função passando o nome do arquivo de consulta como parâmetro
qObj = query.Query(sys.argv[2], ARQ_INDICE, ind.loadBase())
q = qObj.executeQuery()
print(q)
arqResp = open(ARQ_RESPOSTA, 'w')
arqResp.write(str(len(q)) + "\n")
for arq in q:
    arqResp.write(arq + "\n")