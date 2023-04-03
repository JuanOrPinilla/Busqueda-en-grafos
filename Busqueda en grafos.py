########################################################
###                   BFS_CONNECT                    ###
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

def BFS_connect(AdjList, Node1,Node2):
    #paso 1: crear una lista con los nodos del grafo
    llaves = list(AdjList.keys())
    #paso 2: Inicializar un diccionario que tiene como llaves los nodos y el valor False (el boolean indicará si está conectado o no) 
    visitado = {}
    for element in llaves:
        visitado[element] = False
    #paso 3: Iniciar la cola con el nodo de inicio
    queue = [Node1]
    #repetir hasta que se acabe la cola
    while queue:
        nodo_actual = queue.pop(0)
        #paso 4: actualizar el boolean del nodo actual a True (es visitado)
        visitado[nodo_actual] = True
        #paso 5: revisar los nodos a los cuales está conectado el nodo actual y añadirlos a la cola
        for element in AdjList[nodo_actual]:
            if visitado[element] == False:
                queue.append(element)
    #paso 6: retornar el valor del diccionario 'visitado' del Nodo 2
    return visitado[Node2]

print(BFS_connect({1:[2,3,4],2:[1],3:[1,4],4:[3,1]},2,4))

########################################################
###                BFS_shortest_path                 ###
########################################################

"""
¿Cuál es el camino de menor longitud que comunica a Node1,Node2 en el grafo G (representado por AdjList)?

lista de adyacencia = {1:[2,3,4],2:[1],3:[1,4],4:[3,1]}
Node1 = 2
Node2 = 4
Resultado: [2,1,4]

lista de adyacencia = {1:[2,3,4],2:[1],3:[1,4],4:[3,1]}
Node1: 3
Node2: 4
Resultado: [3,4]

lista de adyacencia = {1:[3,4],2:[4],3:[1,4],4:[3,1]}
Node1 = 1
Node2 = 2
Resultado: No hay camino
"""

def BFS_shortest_path(AdjList, Node1, Node2):
    #mismo proceso que BFS_Connect a excepcion de que se inicializa una lista 'camino' para indicar el camino más corto
    camino = []
    camino.append(Node1)
    llaves = list(AdjList.keys())
    visitado = {}
    for element in llaves:
        visitado[element] = False
    #paso 1: la cola recibe tanto el nodo inicial como la lista con el camino más corto
    queue = [(Node1,camino)]
    while queue:
        (nodo, camino) = queue.pop(0)
        for element in AdjList[nodo]:
            if visitado[element] == False:
                visitado[element] = True
                if element == Node2:
                    #si el nodo vecino es igual al nodo de llegada se debe cortar el ciclo y se retorna el camino
                    return camino + [element]
                #en caso de no ser el mismo se agrega a la cola y se repite el proceso
                else:
                    queue.append((element, camino + [element]))
    #si nunca se alcanza el nodo de llegada se asume que no hay un camino existente entre Node 1 y Node 2
    return "No hay camino"

print(BFS_shortest_path({1:[2,3,4],2:[1],3:[1,4],4:[3,1]},2,4))

########################################################
###                   floodFill                      ###
########################################################

"""
El problema consiste en modificar una imagen representada
por una matriz de números enteros m x n, llamada "image"
donde image[i][j] representa el valor del píxel de la imagen.

Se dan tres enteros: sr, sc y color. Estos representan las coordenadas
del punto de inicio del relleno (sr,sc) y el nuevo color (color) con el
que se va a rellenar.

Para realizar el relleno, se considera el píxel de inicio y se buscan 
todos los píxeles adyacentes que tengan el mismo color que el píxel de inicio.
Luego, se busca en esos píxeles adyacentes y se continúa el proceso hasta que
se hayan revisado todos los píxeles conectados 4-direccionalmente.

Matriz = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
Resultado: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

Matriz = [[0,0,0],[0,0,0],[0,0,0]]
sr = 1
sc = 1
color = 3
Resultado: [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
"""

def floodFill(image, sr, sc, color):
    #tamaño n de la matriz
    n = len(image)
    #tamaño m de la matriz
    m = len(image[0])
    #valor de la coordenada inicial
    valor_coordenada_inicial = image[sr][sc]
    #visitado es un diccionario con la coordenada y de valor un boolean que indica si fue visitado o si no
    visitado = {}
    #inicializar el diccionario con todos los valores en False
    for i in range(len(image)):
        for j in range(len(image[0])):
            visitado[(i,j)] = False
    #elemento inicial de la cola es la coordenada inicial
    queue = [(sr, sc)] 
    while queue:
        sr, sc = queue.pop(0)
        #si el valor de la coordenada en el diccionario visitado es False
        if visitado[(sr, sc)] == False:
            #compara si es igual al valor de la coordenada inicial
            if image[sr][sc] == valor_coordenada_inicial:
                #cambia el color de la coordenada
                image[sr][sc] = color
                #lo marca como visitado
                visitado[(sr, sc)] = True
                #agrega las coordenadas adyacentes a la cola
                if sr > 0:
                    queue.append((sr-1, sc))
                if sr < n-1:
                    queue.append((sr+1, sc))
                if sc > 0:
                    queue.append((sr, sc-1))
                if sc < m-1:
                    queue.append((sr, sc+1))
    return image
        
print(floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))

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

########################################################
###                   DFS_isTree                     ###
########################################################

"""
dado un grafo retorne True si el grafo es un arbol, en otro caso False.

Recordar: Un grafo es un árbol si es un grafo conexo y acíclico.
Es decir, todos los vértices del grafo están conectados entre sí y no existen ciclos en el grafo.

lista de adyacencia = {1:[2,3,4],2:[1],3:[1,4],4:[3,1]}
Resultado: False (ciclos)

lista de adyacencia = {1:[2, 3, 4],2:[5, 6],3:[7],4:[],5:[],6:[],7:[8, 9],8:[],9:[],10:[]}
Resultado: False (10 no está conectado)

lista de adyacencia = {1:[2, 3, 4],2:[5, 6],3:[7],4:[],5:[],6:[],7:[8, 9],8:[],9:[]}
Resultado: True
"""
def DFS_isTree(AdjList:dict) -> bool:
    llaves = list(AdjList.keys())
    Nodo_inicial = llaves[0]
    visitado = {}
    for element in llaves:
        visitado[element] = False
    DFS_isTree_recursion(AdjList,Nodo_inicial,visitado)
    for nodo in llaves:
        if visitado[nodo] == False:
            # Si hay un vértice no visitado, entonces el grafo no es un árbol
            return False
    # Si se han visitado todos los vértices, entonces el grafo es un árbol
    return True

def DFS_isTree_recursion(AdjList,Nodo_inicial,visitado,padre=None):
    visitado[Nodo_inicial] = True
    for vecino in AdjList[Nodo_inicial]:
        if visitado[vecino] == False:
            DFS_isTree_recursion(AdjList,vecino,visitado, Nodo_inicial)
        #la unica forma en la que no se pueda considerar un ciclo siendo el nodo visitado es que no sea padre del vertice actual
        elif vecino != padre:
            # Si se encuentra un ciclo, el grafo no es un árbol
            visitado[vecino] = False

print(DFS_isTree({1: [2, 3, 4],2: [5, 6],3: [7],4: [],5: [],6: [],7: [8, 9],8: [],9: []}))