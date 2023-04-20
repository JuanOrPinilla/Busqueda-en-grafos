"""
Este archivo fue creado por Juan Orduz.
Fecha de creación: 20 de abril de 2023
"""
########################################################
###                      bipartito                   ###
########################################################

"""
Un grafo bipartito, es un grafo tal que el conjunto de nodos se puede expresar
como dos conjuntos disjuntos, de manera que no hay dos nodos del mismo conjunto
que sean adyacentes. Diseñe un algoritmo que reciba un grafo, en su implantación
indique si su grafo esta implementado como lista o matriz de adyacencia, y retorne
T rue si el grafo es bipartito y F alse en otro caso. La complejidad no debe superar
O(|V ||E|), donde V es el conjunto de nodos y E el conjunto de arcos del grafo.

lista de adyacencia = {1:[2],2:[3],3:[4],4:[1]}
Retorna: "es bipartito"

lista de adyacencia = {1:[2,3], 2:[1,3],3:[1, 2]}
Retorna: "no es bipartito"

lista de adyacencia = {1:[2, 3],2:[1, 3],3:[1, 2, 4],4:[3, 5],5:[4]}
Retorna: "no es bipartito"
"""

def bipartito(adjList):
    llaves = list(adjList.keys())
    visitado = {}
    for element in llaves:
        visitado[element] = False

    color = {}
    nodo_inicial = 1
    color[1] = 0
    queue = [(nodo_inicial, color[nodo_inicial])]
    while queue:
        nodo_actual,color_padre = queue.pop(0)
        visitado[nodo_actual] = True
        for vecino in adjList[nodo_actual]:
            if visitado[vecino] == False:
                if color_padre == 0:
                    color[vecino] = 1
                elif color_padre == 1:
                    color[vecino] = 0
                queue.append((vecino,color[vecino]))
            elif visitado[vecino] == True:
                if color[vecino] == color_padre:
                    return False
    return True

print(bipartito({1:[2],2:[3],3:[4],4:[1]}))
#print(bipartito({1:[2,3], 2:[1,3],3:[1, 2]}))
#print(bipartito({1:[2, 3],2:[1, 3],3:[1, 2, 4],4:[3, 5],5:[4]}))
