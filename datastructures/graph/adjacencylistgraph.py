class AdjNode:
    def __init__(self, vertex, dist) -> None:
        self.vertex = vertex
        self.dist = dist
        self.next = None

    def __str__(self) -> str:
        return f'Vertex: {self.vertex} Distance: {self.dist}'

class AdjacencyListGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_node(self, src, dest, dist):
        node = AdjNode(dest, dist)
        if self.graph[src] is None:
            self.graph[src] = node
        else:
            head = self.graph[src] 
            while head.next:
                head = head.next
            head.next = node
    
    def print_graph(self):
        for index, vertex in enumerate(self.graph):
            if vertex is None:
                continue
            print(f'Vertex {index} connected to:')
            while vertex:
                print(f'    {vertex}')
                vertex = vertex.next
    
    def egde_dist(self, src: int, dest: int) -> int:
        for node in self.get_linked_nodes(src):
            if node.vertex == dest:
                return node.dist    
        return -1

    def get_nodes(self):
        return [x for x in range(self.V)]

    def get_linked_nodes(self, src):
        node = self.graph[src]
        while node:
            yield node
            node = node.next

if __name__ == '__main__':
    
    graph = Graph(3)
    graph.add_node(src=0, dest=2, dist=100)
    graph.add_node(src=0, dest=1, dist=19)
    graph.add_node(src=1, dest=2, dist=99)
    graph.add_node(src=2, dest=1, dist=3)
    graph.print_graph()