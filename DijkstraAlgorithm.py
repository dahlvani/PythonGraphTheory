#Dijkstra algorithm in a graph
def Dijkstra(graph, node):

    distance = {}
    distance[node] = 0
    path = {}
    while (distance):
        # in case we have a disjoint graph
        op_node = min_distance(distance)
        path[op_node] = distance[op_node]
        del distance[op_node]
        for x, x_len in graph[op_node].items():
            if x not in path:
                if x not in distance:
                    distance[x] = path[op_node] + x_len
                elif distance[x] > path[op_node] + x_len:
                    distance[x] = path[op_node] + x_len
    return path
