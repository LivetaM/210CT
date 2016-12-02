class vertex(object):
    def __init__(self, label, edges=[]):
        self.label = label
        self.edges = []
        
class creating_Graph(object):
    def __init__(self):
        self.graph_List = []

    def add_vertex(self, v): #v - vertex
        self.graph_List.append(v)

    def create_Edges(self, v1, v2): #v1 - vertex1 and v2 - vertex2
        for i in self.graph_List:
            if v1 in i.edges and i!=v2:
                pass
            else:
                i.edges.append(v1)
            if v2 in i.edges and i!=v1:
                pass
            else:
                i.edges.append(v2)
                
                

def dijkstra(graph, source, destination):
    v = source
    for n in graph.graph_List:
        n.tw = float('inf')
    source.tw=0
    visited = []
    while v != destination:
        for u in v.edges:
            if v.tw+v[u].w < u.tw:
                u.tw=v.tw+v[u].w
                u.pre = v
        visited.append(v)
        minimum = float('inf')
        for n in v:
            if n not in visited and n.tw <minimum:
                v=n
                minimum=n.tw


vertex1 = vertex(1)
vertex2 = vertex(2)
vertex3 = vertex(3)
vertex4 = vertex(4)
vertex5 = vertex(5)
g = creating_Graph() #g stands for graph
g.add_vertex(vertex1)
g.add_vertex(vertex2)
g.add_vertex(vertex3)
g.add_vertex(vertex4)
g.add_vertex(vertex5)
g.create_Edges(vertex1, vertex4)
g.create_Edges(vertex4, vertex2)
g.create_Edges(vertex5, vertex3)
g.create_Edges(vertex1, vertex3)                  
visited = dijkstra(g, vertex3, vertex5)
vertex = vertex5
while vertex.pre!=None:
    print(vertex.pre.label)
    vertex=vertex.pre
