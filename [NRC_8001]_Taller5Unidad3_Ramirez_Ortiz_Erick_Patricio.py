def busqueda_general(grafo, costo, inicio, meta):
	"""
	Funcion que realiza la busqueda general desde el nodo de inicio hasta el nodo meta retornando el valor del costo por la busqueda realizada.
 	Parámetros
  	--------------------
   	grafo: grafo que está formado por una lista de listas
	costo: diccionario que contiene el costo de cada conexion de los nodos del grafo
 	inicio: nodo desde donde se va a iniciar la búsqueda.
  	meta: nodo a donde se desea llegar.
   	Retorno
   	--------------------
   	costo_actual: valor del costo obtenido al realizar la busqueda
	None: Si no se encuentra un camino desde el nodo de inicio hasta el nodo de destino
 	"""
	# Declaramos una lista vacía visitado para almacenar los nodos visitados durante la búsqueda.
	visitado = []
	#Creamos una lista cola con un solo elemento que es una tupla que contiene el nodo de inicio y un costo de 0.
	cola = [(inicio, 0)]
    #Inicia un bucle while con la condición cola que ejecuta las siguientes operaciones mientras la cola no esté vacía.
	while cola:
		#Asigna a las variables nodo y costo_actual los valores del último elemento de la lista cola y lo elimina de la misma.
		nodo, costo_actual = cola.pop(0)
		#Verificamos si nodo es igual a la meta deseada, si es así, devolvemos el costo total obtenido
		if nodo == meta:
			#Retornamos el costo
			return costo_actual,visitado
       #Verificamos si nodo no está en la lista de visitado
		if nodo not in visitado:
			#Si es asi agregamos ese nodo a la lista de visitado
			visitado.append(nodo)
			#Bucle for para cada vecino en grafo[nodo]
			for vecino in grafo[nodo]:
				 #se agrega a la lista cola una tupla con el vecino y un costo actualizado de costo_actual + cost[(node, neighbor)].
				cola.append((vecino, costo_actual + costo[(nodo, vecino)]))
    #Retornamos el valor de none si no se encuentra un camino desde el nodo de inicio hasta el nodo de destino
	return None

if __name__ == "__main__":
	# creación del grafo y diccionario de costos
	graph,cost = [[] for i in range(9)],{}
	#Imprimimos el nodo y el grafo en modo de lista de listas y en un diccionario para los costos
	print(graph, cost)
	# añadir los nodos
	#0 a p1
	graph[0].append(1)
	graph[1].append(0)
	#p1 a p4
	graph[1].append(4)
	graph[4].append(1)
	#p1 a p8
	graph[1].append(8)
	graph[8].append(1)
	#p4 a p5
	graph[4].append(5)
	graph[5].append(4)
	#p4 a p7
	graph[4].append(7)
	graph[7].append(4)
	#p5 a p3
	graph[5].append(3)
	graph[3].append(5)
	#p7 a p2
	graph[7].append(2)
	graph[2].append(7)
	#p2 a p3
	graph[2].append(3)
	graph[3].append(2)
	#p2 a p6
	graph[2].append(6)
	graph[6].append(2)
	#p6 a p8
	graph[6].append(8)
	graph[8].append(6)
	#p6 a p3
	graph[6].append(3)
	graph[3].append(6)
	#p3 a p8
	graph[3].append(8)
	graph[8].append(3)#

    # añadiendo el costo a los nodos, todos con el valor de 1
	cost[(0, 1)] = cost[(1, 0)] = cost[(1, 4)]= cost[(4, 1)]= cost[(0, 1)]= cost[(1, 8)]= cost[(8, 1)]= cost[(4, 5)]= cost[(5, 4)]= cost[(4, 7)]= cost[(7, 4)]= cost[(5, 3)]= cost[(3, 5)]= cost[(7, 2)]= cost[(2, 7)]= cost[(2, 3)]= cost[(3, 2)]= cost[(2, 6)]= cost[(6, 2)]= cost[(6, 8)]= cost[(8, 6)]= cost[(6, 3)]= cost[(3, 6)]= cost[(3, 8)]= cost[(8, 3)] = 1
	
	#Imprimimos el nodo y el grafo en modo de lista de listas y en un diccionario para los costos
	print(graph, cost)
	# establecer el estado objetivo
	meta = 6
	
	# establecer el nodo inicial
	inicio = 0
	#Imprimimos el el costo total obtenido desde el nodo de inicio hasta el nodo meta
	costo,camino = busqueda_general(graph, cost, inicio, meta)
	print(f"Minimo costo del nodo {inicio} al nodo {meta} es {costo}")
	print(f"Camino recorrido: {camino}")

