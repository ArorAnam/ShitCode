from collections import deque

# matrix_traversals.py

def traverse_matrix_dfs(matrix):
    def dfs(i, j):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or (i, j) in visited:
            return
        visited.add((i, j))
        print(matrix[i][j], end=' ')
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(i + x, j + y)

    visited = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i, j) not in visited:
                dfs(i, j)
    print()

def traverse_matrix_bfs(matrix):
    queue = deque([(0, 0)])
    visited = set((0, 0))
    while queue:
        i, j = queue.popleft()
        print(matrix[i][j], end=' ')
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + x, j + y
            if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and (ni, nj) not in visited:
                visited.add((ni, nj))
                queue.append((ni, nj))
    print()

def traverse_matrix_spiral(matrix):
    if not matrix:
        return
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            print(matrix[top][j], end=' ')
        top += 1
        for i in range(top, bottom + 1):
            print(matrix[i][right], end=' ')
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                print(matrix[bottom][j], end=' ')
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left], end=' ')
            left += 1
    print()

def traverse_matrix_diagonal(matrix):
    m, n = len(matrix), len(matrix[0])
    for d in range(m + n - 1):
        if d < n:
            i, j = 0, d
        else:
            i, j = d - n + 1, n - 1
        while i < m and j >= 0:
            print(matrix[i][j], end=' ')
            i += 1
            j -= 1
    print()

# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("DFS Traversal:")
    traverse_matrix_dfs(matrix)
    print("BFS Traversal:")
    traverse_matrix_bfs(matrix)
    print("Spiral Traversal:")
    traverse_matrix_spiral(matrix)
    print("Diagonal Traversal:")
    traverse_matrix_diagonal(matrix)