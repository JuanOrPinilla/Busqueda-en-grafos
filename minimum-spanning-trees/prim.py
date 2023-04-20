########################################################
###                       prim                       ###
########################################################
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
        
#prim([[0, 2, 3, 0, 0, 5],[2, 0, 0, 2, 0, 0],[3, 0, 0, 1, 5, 0],[0, 2, 1, 0, 0, 1],[0, 0, 5, 0, 2, 0],[5, 0, 0, 1, 0, 0]],0)
prim([[0, 2, 3, 0, 0, 5,0],[2, 0, 0, 2, 0, 0,0],[3, 0, 0, 1, 5, 0,0],[0, 2, 1, 0, 0, 1,0],[0, 0, 5, 0, 2, 0,0],[5, 0, 0, 1, 0, 0,0],[0, 0, 0, 0, 0, 0,0]],0)