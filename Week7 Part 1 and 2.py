import queue
import sys
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
                
                
def breadth_First_Search(G,v):
    Q = queue.Queue()
    visited = []
    Q.put(v)
    while Q:
        u = Q.get()
        if u not in visited:
            visited.append(u)
            for e in u.edges:
                Q.put(e)
    return (visited)

def depth_First_Search(G,v):
    S = []
    visited = []
    S.append(v)
    while S:
        u = S.pop() #takes the last integer from S
        if u not in visited:
            visited.append(u)
            for e in u.edges:
                S.append(e)
                
    return (visited)


def display_The_Result():
    for x in g.graph_List:
        w =  open('Nodes.txt', 'a') # Creates or opens a file
        w.write(str(x.label) +'\n') # writes into a file
        w.close()
        
    for n in depth_First_Search(g,x):
        w =  open("DFS.txt", 'a') # Creates or opens a file
        w.write(str(n.label) + '\n') # writes into a file
        w.close()
        
    for m in breadth_First_Search(g,x):
        w =  open("BFS.txt", 'a') # Creates or opens a file
        w.write(str(m.label) + '\n') # writes into a file
        w.close()
        


  
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
g.create_Edges(vertex1, vertex2)
g.create_Edges(vertex3, vertex2)
g.create_Edges(vertex3, vertex4)
g.create_Edges(vertex4, vertex1)
g.create_Edges(vertex1, vertex5)
display_The_Result()
  
