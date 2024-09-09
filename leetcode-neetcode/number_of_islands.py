from typing import List
import collections

def numberofIslands(grid: List[List[int]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands_cnt = 0

    def bfs(r, c): #iterative
        q = collections.deque() 
        visited.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft() # q.pop for DFS approach
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and
                    c in range(cols) and
                    grid[r][c] == "1" and
                    (r, c) not in visited
                    ):
                    q.append(r, c)
                    visited.add(r, c)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r,c) not in visited:
                bfs(r, c)
                islands_cnt += 1

    return islands_cnt