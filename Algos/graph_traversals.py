from collections import deque

# /Users/namanarora/Documents/Leetcode/Algos/graph_traversals.py


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        self._dfs_util(start, visited)
    
    def _dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph.get(v, []):
            if neighbour not in visited:
                self._dfs_util(neighbour, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            v = queue.popleft()
            print(v, end=' ')
            for neighbour in self.graph.get(v, []):
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("DFS starting from vertex 2:")
    g.dfs(2)

    print("\nBFS starting from vertex 2:")
    g.bfs(2)