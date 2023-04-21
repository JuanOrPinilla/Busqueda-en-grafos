########################################################
###                       prim                       ###
########################################################
"""
El algoritmo de Prim es un algoritmo de tipo voraz (greedy) utilizado para encontrar el árbol de expansión mínimo (MST) 
de un grafo no dirigido y con pesos. El MST es un subconjunto de aristas que conectan todos los vértices del grafo, 
y tiene el menor peso total posible.

matrizAdyacencias = [[0, 2, 3, 0, 0, 5],[2, 0, 0, 2, 0, 0],[3, 0, 0, 1, 5, 0],[0, 2, 1, 0, 0, 1],[0, 0, 5, 0, 2, 0],[5, 0, 0, 1, 0, 0]]
Node1 = 0
Resultado:
1-2:2
2-4:2
4-3:1
4-6:1
3-5:5

"""
def prim(adjMatriz,Node1):
    INF = 9999999
    # number of vertices in graph
    N = len(adjMatriz[0])
    visitado = [0]*N
    no_edge = 0
    visitado[Node1] = True
    print("Nodo : arco")
    while (no_edge < N - 1):
        minimum = INF
        for nodo in range(N):
            if visitado[nodo]:
                for vecino in range(N):
                    if ((not visitado[vecino]) and adjMatriz[nodo][vecino]):  
                        # not in selected and there is an edge
                        if minimum > adjMatriz[nodo][vecino]:
                            minimum = adjMatriz[nodo][vecino]
                            a = nodo
                            b = vecino
        print(str(a+1) + "-" + str(b+1) + ":" + str(adjMatriz[a][b]))
        visitado[b] = True
        no_edge += 1
        
prim([[0, 2, 3, 0, 0, 5],[2, 0, 0, 2, 0, 0],[3, 0, 0, 1, 5, 0],[0, 2, 1, 0, 0, 1],[0, 0, 5, 0, 2, 0],[5, 0, 0, 1, 0, 0]],0)
#prim([[0, 2, 3, 0, 0, 5,0],[2, 0, 0, 2, 0, 0,0],[3, 0, 0, 1, 5, 0,0],[0, 2, 1, 0, 0, 1,0],[0, 0, 5, 0, 2, 0,0],[5, 0, 0, 1, 0, 0,0],[0, 0, 0, 0, 0, 0,0]],0)