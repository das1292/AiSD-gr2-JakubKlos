from projekt import Queue
from enum import *
from typing import *
import networkx as nx
import matplotlib.pyplot as plt


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self,data,index):
        self.data=data
        self.index=index

    def __repr__(self):
        return f'{self.data}:v{self.index}'

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self,source,destination,weight):
        self.source=source
        self.destination=destination
        self.weight=weight

class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies=dict()

    def __repr__(self):
        str=""
        for data in self.adjacencies:
            str+=f'-{data}->{self.adjacencies[data]}\n'
        return str

    def create_vertex(self, value):
        vertex=Vertex(value,len(self.adjacencies))
        self.adjacencies[vertex]=[]

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        edge=Edge(source, destination, weight)
        self.adjacencies[edge.source].append((edge.destination))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        edge=Edge(source, destination, weight)
        self.adjacencies[edge.source].append((edge.destination))
        self.adjacencies[edge.destination].append((edge.source))

    def add(self,edge:EdgeType,source:Vertex,destination:Vertex,weight:Optional[float]=None):
        if edge.name=="directed":
            self.add_directed_edge(source,destination,weight)
        else:
            self.add_undirected_edge(source,destination,weight)

    def traverse_breadth_first(self,visit:Callable[[Any],None]):
        queue=Queue()
        vertices=list(graf1.adjacencies.keys())
        visited=[vertices[0]]
        queue.enqueue(vertices[0])
        while len(queue):
            x=queue.dequeue()
            visit(x)
            visited.append(x)
            for neighbour in self.adjacencies[x]:
                if neighbour.destination not in visited:
                    visited.append(neighbour.destination)
                    queue.enqueue(neighbour.destination)

    def dfs(self,V:Vertex,visited:List[Vertex],visit:Callable[[Any],None]):
        visit(V)
        visited.append(V)
        for neighbour in self.adjacencies[V]:
            if neighbour.destination not in visited:
                self.dfs(neighbour.destination,visited,visit)

    def traverse_depth_first(self,visit:Callable[[Any],None]):
        vertices=list(graf1.adjacencies.keys())
        visited=[]
        self.dfs(vertices[0],visited,visit)

    def show(self):
        x=nx.DiGraph()
        y=[]
        for source in self.adjacencies:
            for (destination) in self.adjacencies[source]:
                y.append((source,destination))
                x.add_edges_from(y)
        pos=nx.spring_layout(x)
        nx.draw_networkx(x,pos,arrows=True,node_size=1000)
        labels=nx.get_edge_attributes(x,'weight')
        nx.draw_networkx_edge_labels(x,pos,edge_labels=labels)
        plt.show()

def mutual_friends(g: Graph, f0: Any, f1: Any) -> List[Any]:
    x=[]
    for value in g.adjacencies[f0]:
        for value2 in g.adjacencies[f1]:
            if value==value2:
                    x.append(value)
    return x

graf1 = Graph()

graf1.create_vertex("VI")
graf1.create_vertex("RU")
graf1.create_vertex("PA")
graf1.create_vertex("CO")
graf1.create_vertex("CH")
graf1.create_vertex("RA")
graf1.create_vertex("SU")
graf1.create_vertex("KE")


vertex = list(graf1.adjacencies.keys())

graf1.add_undirected_edge(vertex[0], vertex[4])
graf1.add_undirected_edge(vertex[0], vertex[1])
graf1.add_undirected_edge(vertex[0], vertex[2])
graf1.add_undirected_edge(vertex[1], vertex[5])
graf1.add_undirected_edge(vertex[1], vertex[2])
graf1.add_undirected_edge(vertex[1], vertex[0])
graf1.add_undirected_edge(vertex[2], vertex[3])
graf1.add_undirected_edge(vertex[2], vertex[7])
graf1.add_undirected_edge(vertex[3], vertex[2])
graf1.add_undirected_edge(vertex[3], vertex[0])


graf1.show()
print(mutual_friends(graf1,vertex[1],vertex[3]))


graf2 = Graph()

graf2.create_vertex("VI")
graf2.create_vertex("RU")
graf2.create_vertex("PA")
graf2.create_vertex("CO")
graf2.create_vertex("CH")
graf2.create_vertex("RA")
graf2.create_vertex("SU")
graf2.create_vertex("KE")

vertex = list(graf2.adjacencies.keys())

graf2.add_undirected_edge(vertex[0], vertex[4])
graf2.add_undirected_edge(vertex[0], vertex[1])
graf2.add_undirected_edge(vertex[0], vertex[2])
graf2.add_undirected_edge(vertex[1], vertex[4])
graf2.add_undirected_edge(vertex[1], vertex[3])
graf2.add_undirected_edge(vertex[1], vertex[2])
graf2.add_undirected_edge(vertex[2], vertex[5])
graf2.add_undirected_edge(vertex[2], vertex[7])
graf2.add_undirected_edge(vertex[3], vertex[1])
graf2.add_undirected_edge(vertex[3], vertex[4])


graf2.show()
print(mutual_friends(graf2,vertex[3],vertex[2]))

graf3 = Graph()

graf3.create_vertex("VI")
graf3.create_vertex("RU")
graf3.create_vertex("PA")
graf3.create_vertex("CO")
graf3.create_vertex("CH")
graf3.create_vertex("RA")
graf3.create_vertex("SU")
graf3.create_vertex("KE")


vertex = list(graf3.adjacencies.keys())

graf3.add_undirected_edge(vertex[0], vertex[1])
graf3.add_undirected_edge(vertex[0], vertex[2])
graf3.add_undirected_edge(vertex[0], vertex[3])
graf3.add_undirected_edge(vertex[1], vertex[5])
graf3.add_undirected_edge(vertex[1], vertex[6])
graf3.add_undirected_edge(vertex[1], vertex[7])
graf3.add_undirected_edge(vertex[2], vertex[6])
graf3.add_undirected_edge(vertex[2], vertex[5])
graf3.add_undirected_edge(vertex[3], vertex[1])
graf3.add_undirected_edge(vertex[3], vertex[0])

graf3.show()
print(mutual_friends(graf3,vertex[3],vertex[0]))