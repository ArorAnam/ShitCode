from collections import deque

# Time: O(m * n)
# Space: O(m * n)

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # get the dimentions
        rows, cols = len(matrix), len(matrix[0])
        # ans matrix
        distance_matrix = [[-1] * cols for _ in range(rows)]
        # queue to store indices 0s
        queue = deque()

        # go through the mateix to find all 0s
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    distance_matrix[i][j] = 0
                    queue.append((i, j))
        
        # initialize the driections of movement
        # up, left, down, right
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))

        # process the queue, bfs
        while queue:
            i, j = queue.popleft()
            # explore all directions
            for delta_i, delta_j in directions:
                neighbour_i, neighbour_j = i + delta_i, j + delta_j
                # if neighbour is within the bounds and hasn't been visited
                if 0 <= neighbour_i < rows and 0 <= neighbour_j < cols \
                        and distance_matrix[neighbour_i][neighbour_j] == -1:
                    # update the distance for this neigbour
                    distance_matrix[neighbour_i][neighbour_j] = distance_matrix[i][j] + 1
                    # add this neighbour to the queue for further exploration
                    queue.append((neighbour_i, neighbour_j))
        
        # return the update matrix
        return distance_matrix