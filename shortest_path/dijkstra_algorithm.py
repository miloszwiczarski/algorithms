import sys
sys.path.append('/Users/Kuba/Desktop/ALGO')
from datastructures.queue import Queue
from datastructures.graph.adjacencylistgraph import Graph


A = 0
B = 1
C = 2
D = 3
E = 4


def dijkstra_algorithm(graph: Graph, source: int) -> int:

    nodes = graph.get_nodes()
    dist = []
    prev = []
    q = Queue()

    for node in nodes:
        dist.append(sys.maxsize)
        prev.append(None)
        q.push(node)

    dist[source] = 0

    while not q.is_empty():
        min_dist = sys.maxsize
        node_with_min_dist = -1
        # Graph is a list of linked lists we need to traverse them
        # to find the lowest distance from node to source

        print(dist)
        print(prev)

        print(q.get_queue())
        for q_node in q.get_queue():
            if q_node == source:
                continue
            
            for node in graph.get_linked_nodes(src=q_node):
                print(node)
                if node.dist < min_dist:
                    min_dist = node.dist
                    node_with_min_dist = node.vertex

            print(node_with_min_dist)
            
            
            for node in graph.get_linked_nodes(src=node_with_min_dist):
                if not q.is_in_q(node.vertex):
                    continue
                
                print(node)
                alt = dist[node_with_min_dist] + graph.egde_dist(node_with_min_dist, node.vertex)

                if alt < dist[node.vertex]:
                    dist[node.vertex] = alt 
                    prev[node.vertex] = node.vertex

        q.remove(node_with_min_dist)


graph = Graph(5)
graph.add_node(src=A, dest=B, dist=4)
graph.add_node(src=A, dest=C, dist=2)
graph.add_node(src=B, dest=D, dist=2)
graph.add_node(src=B, dest=C, dist=3)
graph.add_node(src=C, dest=E, dist=5)
graph.add_node(src=C, dest=D, dist=4)
graph.add_node(src=E, dest=D, dist=1)
dijkstra_algorithm(graph, A)
