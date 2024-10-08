from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    
    def add_edge(self, u, v, w):
        self.edges[u][v] = w
        self.edges[v][u] = w
    
def dijstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbour in range(graph.v):
            if graph.edges[current_vertex][neighbour] != -1:
                distance = graph.edges[current_vertex][neighbour]
                if neighbour not in graph.visited:
                    old_cost = D[neighbour]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbour))
                        D[neighbour] = new_cost
        
    return D

# if __name__ == '__main__':
#     g = Graph(9)
#     g.add_edge(0, 1, 4)
#     g.add_edge(0, 6, 7)
#     g.add_edge(1, 6, 11)
#     g.add_edge(1, 7, 20)
#     g.add_edge(1, 2, 9)
#     g.add_edge(2, 3, 6)
#     g.add_edge(2, 4, 2)
#     g.add_edge(3, 4, 10)
#     g.add_edge(3, 5, 5)
#     g.add_edge(4, 5, 15)
#     g.add_edge(4, 7, 1)
#     g.add_edge(4, 8, 5)
#     g.add_edge(5, 8, 12)
#     g.add_edge(6, 7, 1)
#     g.add_edge(7, 8, 3) 
    
#     D = dijstra(g, 0)
#     # print(D)

#     for vertex in range(len(D)):
#         print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])

# Time complexity: O(|E| + |V|log|V|) where E is the number of edges and V is the number of vertices
# Here we pass each edge once and each vertex once to the priority queue. The priority queue has a time complexity of O(log|V|) for each insertion and deletion.
# But sorting in priority queue is done in O(VlogV) time. So the overall time complexity is O(|E| + |V|log|V|)
# Space complexity: O(V) where V is the number of vertices

from typing import List
from collections import defaultdict
import heapq
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    pq = [(0, k)]
    dist = {}
    
    while pq:
        d, node = heapq.heappop(pq)
        if node in dist:
            continue
        dist[node] = d
        for nei, d2 in graph[node]:
            if nei not in dist:
                heapq.heappush(pq, (d+d2, nei))
    
    return max(dist.values()) if len(dist) == n else -1
