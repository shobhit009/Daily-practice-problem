class Graph:
    def __init__(self, v, is_directed=False):
        self.v = v
        self.adj_list = {}
        self.is_directed = is_directed

        for i in range(v):
            self.adj_list[i] = []

    def add_edge(self, source,destination):
       self.adj_list[source].append(destination)

       if self.is_directed == False:
           self.adj_list[destination].append(source)

        
    def print_adj_list(self):
        for i in range(len(self.adj_list)):
            print(i,"->",self.adj_list[i])
       

if __name__ == "__main__":
    graph =Graph(4)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,2)
    graph.add_edge(1,3)
    graph.print_adj_list()