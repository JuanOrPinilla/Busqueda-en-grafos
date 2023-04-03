########################################################
###                   DFS_CONNECT                    ###
########################################################

"""
¿Existe algún camino que conecte a Node1 y Node2 en el grafo G (representado por AdjList)?

lista de adyacencia = {1:[2,3,4],2:[1],3:[1,4],4:[3,1]}
Node1 = 2
Node2 = 4
Resultado: True

lista de adyacencia = {1:[2],2:[1],3:[1,4],4:[3,1]}
Node1 = 2
Node2 = 4
Resultado: False
"""

def DFS_connect(AdjList:dict, Node1:int,Node2:int)-> bool:
    llaves = list(AdjList.keys())
    visitado = {}
    for element in llaves:
        visitado[element] = False
    DFS_recursion(AdjList,Node1,visitado)
    return visitado[Node2]

def DFS_recursion(AdjList,Node1,visitado):
    visitado[Node1] = True
    for vecino in AdjList[Node1]:
        if visitado[vecino] == False:
            DFS_recursion(AdjList,vecino,visitado)

print(DFS_connect({1:[2,3,4],2:[1],3:[1,4],4:[3,1]},2,4))