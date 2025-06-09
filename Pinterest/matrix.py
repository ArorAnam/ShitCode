def longestIncreasingPath(matrix):
    """
    Given an m x n integers matrix, return the length of the longest increasing path in matrix.
    From each cell, you can either move in four directions: left, right, up, or down.
    You may NOT move diagonally or move outside the boundary.
    """
    if not matrix or not matrix[0]:
        return 0
        
    rows, cols = len(matrix), len(matrix[0])
    # Cache to store computed results
    dp = [[0] * cols for _ in range(rows)]
    
    def dfs(i, j, prev):
        # Check bounds and if current cell is smaller than previous
        if (i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] <= prev):
            return 0
            
        # If already computed, return cached result
        if dp[i][j]:
            return dp[i][j]
            
        # Try all four directions
        current = matrix[i][j]
        left = dfs(i, j-1, current)
        right = dfs(i, j+1, current) 
        up = dfs(i-1, j, current)
        down = dfs(i+1, j, current)
        
        # Store max path length starting from current cell
        dp[i][j] = 1 + max(left, right, up, down)
        return dp[i][j]
    
    # Try starting from each cell
    max_path = 0
    for i in range(rows):
        for j in range(cols):
            max_path = max(max_path, dfs(i, j, float('-inf')))
            
    return max_path

if __name__ == "__main__":
    # Test cases
    matrix1 = [
        [9,9,4],
        [6,6,8],
        [2,1,1]
    ]
    print(longestIncreasingPath(matrix1))  # Output: 4
    # Explanation: The longest increasing path is [1,2,6,9]
    
    matrix2 = [
        [3,4,5],
        [3,2,6],
        [2,2,1]
    ]
    print(longestIncreasingPath(matrix2))  # Output: 4
    # Explanation: The longest increasing path is [3,4,5,6]
    
    matrix3 = [[1]]
    print(longestIncreasingPath(matrix3))  # Output: 1
