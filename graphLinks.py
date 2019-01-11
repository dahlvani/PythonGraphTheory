
#Checks whether a node is in a graph
def checkNode(node, graph):

    if node in graph:
        return(True)
    else:
        return (False)

#Takes a list of links (tuples, lists) with two elements describing the connected nodes and returns a dictionary graph
def fromLinks(links):
    # initialize empty dictionary
    graph = {}
    #iterate through input nodes
    for link in links:
        #Checks node is in the graph, and if it isnt adds it.
        for node in link:
            if not checkNode(node, graph):
                graph[node] = []
        ##for both ends of the node add the link to the other
        graph[link[0]].append(link[1])
        graph[link[1]].append(link[0])
    return graph

#test case runs
assert(fromLinks([(1,2),(1,4),(2,3),(3,4)]) == {1:[2,4],2:[1,3],3:[2,4],4:[1,3]})
