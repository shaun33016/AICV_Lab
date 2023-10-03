from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, vertex, neighbor):
        self.graph[vertex].append(neighbor)
    
    def bfs(self, start_vertex):
        visited = set()
        queue = deque()
        
        visited.add(start_vertex)
        queue.append(start_vertex)
        
        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=' ')
            
            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
print("BFS traversal starting from 'A':")
g.bfs('A')
