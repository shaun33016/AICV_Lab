class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, vertex, neighbor):
        if vertex in self.graph:
            self.graph[vertex].append(neighbor)
        else:
            self.graph[vertex] = [neighbor]
    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        
        if start_vertex not in visited:
            print(start_vertex, end=' ')
            visited.add(start_vertex)
            
            if start_vertex in self.graph:
                for neighbor in self.graph[start_vertex]:
                    self.dfs(neighbor, visited)
g = Graph()
g.add_edge('E', 'A')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
print("DFS traversal starting from 'A':")
g.dfs('B')
