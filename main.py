
def busqueda_general(goal, start):
	pass

# main function
if __name__ == '__main__':

    # create the graph
    graph,cost = [[] for i in range(8)],{}

    # graph is a list of lists. Each element of the outer list corresponds to a node 
    # and the respective inner list holds the neighboring nodes

    # cost is a dictionary

    print(graph, cost)

    # añadir los nodos
    graph[0].append(1)
    graph[1].append(8)
    graph[1].append(4)
    graph[7].append(6)
    graph[7].append(3)
    graph[6].append(3)
    graph[6].append(2)
    graph[2].append(3)
    graph[2].append(7)
    graph[7].append(4)
    graph[4].append(5)
    graph[5].append(3)

    # add the cost
    cost[(0, 1)] = 2
    cost[(1, 8)] = 3
    cost[(1, 4)] = 3
    cost[(7, 6)] = 8
    cost[(7, 3)] = 4
    cost[(6, 3)] = 1
    cost[(6, 2)] = 8
    cost[(2, 3)] = 3
    cost[(2, 7)] = 2
    cost[(7, 4)] = 8
    cost[(4, 5)] = 3
    cost[(5, 3)] = 2

    print(graph, cost)

    # goal state
    goal = []

    # establecimos la meta objetivo en 3
    # there can be multiple goal states
    goal.append(3)

    # get the answer
   # answer = busqueda_general(goal, 0)

    # print the answer
    print("Minimo costo del nodo 0 al nodo 3 es = ")
