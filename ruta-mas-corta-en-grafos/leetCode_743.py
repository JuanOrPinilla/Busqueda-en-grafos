"""
Este archivo fue creado por Juan Orduz.
Fecha de creación: 20 de abril de 2023
"""
####################################################################################
###                             Network Delay Time                               ###
####################################################################################
"""
You are given a network of n nodes, labeled from 1 to n. 
You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node,
vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. 
Return the minimum time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.

Constraints:
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

Examples:

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
Resultado: 2

times = [[1,2,1]]
n = 2
k = 1
Resultado: 1

times = [[1,2,1]]
n = 2
k = 2
Resultado:-1

"""
def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
        #k = nodo incial
        cola_prioridad = [(k,0)]

        #camino: guardar los valores de los costos minimos
        camino = {}
        camino[k] = 0
        #asegurar que todos los vertices son alcanzables
        visitado = {}
        for i in range(1, n+1):
            visitado[i] = False
        
        while cola_prioridad:
            nodo_actual, peso_actual = cola_prioridad.pop(0)
            pesos = []
            vecino = []
            visitado[nodo_actual] = True
            for time in times:
                if time[0] == nodo_actual:
                    pesos.append((peso_actual + time[2]))
                    vecino.append(time[1])
            if len(pesos)>0:
                menor_peso = min(pesos)
                for i in range (len(pesos)):
                    if pesos[i] == menor_peso:
                        cola_prioridad.append((vecino[i],menor_peso))
                        camino[vecino[i]] = menor_peso
        valores_visitado = visitado.values()
        for visita in valores_visitado:
            if visita == False:
                return -1
        return (max(camino.values()))
    
print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))