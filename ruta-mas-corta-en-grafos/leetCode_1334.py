"""
Este archivo fue creado por Juan Orduz.
Fecha de creación: 20 de abril de 2023
"""
####################################################################################
###  Find the City With the Smallest Number of Neighbors at a Threshold Distance ###
####################################################################################

"""
There are n cities numbered from 0 to n-1. 
Given the array edges where edges[i] = [fromi, toi, weighti] 
represents a bidirectional and weighted edge between cities fromi and toi, 
and given the integer distanceThreshold.

Return the city with the smallest number of cities 
that are reachable through some path and whose distance is at most distanceThreshold, 

If there are multiple such cities, return the city with the greatest number.
Notice that the distance of a path connecting cities i and j is 
equal to the sum of the edges' weights along that path.

n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
Resultado: 3

n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2

El intento de implementación es de dijkstra pero recorriendo abosulatemente todos los nodos.

No se usa bellman ford ni wharshall por terminos de complejidad temporal

dadas las siguientes restricciones: 

a2 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti, distanceThreshold <= 10^4
All pairs (fromi, toi) are distinct.

No hay pesos negativos, no hay que preocuparse por eso
"""
def findTheCity(n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        totalCitiesArray = []
        for i in range(n):
            totalCities = 0
            priorityQ = [(i,0)]
            visited = []
            for j in range(n):
                visited.append(False)
            while priorityQ:
                actual_node, actual_peso = priorityQ.pop(0)
                visited[actual_node] = True
                pesos = []
                nodos = []
                for edge in edges:
                    if edge[0] == actual_node and visited[edge[1]] == False:
                        pesos.append(actual_peso + edge[2])
                        nodos.append(edge[1])
                        visited[edge[1]] = True
                        if actual_peso + edge[2] <= distanceThreshold:
                            totalCities += 1
                    elif edge[1] == actual_node and visited[edge[0]] == False:
                        pesos.append(actual_peso + edge[2])
                        nodos.append(edge[0])
                        visited[edge[0]] = True
                        if actual_peso + edge[2] <= distanceThreshold:
                            totalCities += 1
                if len(pesos) > 0:
                    min_peso = min(pesos)
                    indice = pesos.index(min_peso)
                    priorityQ.append((nodos[indice],min_peso))
                    pesos.append(min_peso)
            totalCitiesArray.append(totalCities)
        menor = n
        for element in totalCitiesArray:
            if element <= menor:
                menor = element
        last_index = -1
        for i in range(len(totalCitiesArray)):
            if totalCitiesArray[i] == menor:
                last_index = i
        return last_index
    
print(findTheCity(4,[[0,1,3],[1,2,1],[1,3,4],[2,3,1]],4))