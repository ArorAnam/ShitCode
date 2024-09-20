def minCostConnectPoints(points):
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    def distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    n = len(points)
    parent = list(range(n))
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((distance(points[i], points[j]), i, j))
    edges.sort()

    res, count = 0, 0
    for edge in edges:
        cost, x, y = edge
        if find(x) != find(y):
            union(x, y)
            res += cost
            count += 1
            if count == n - 1:
                break
    return res