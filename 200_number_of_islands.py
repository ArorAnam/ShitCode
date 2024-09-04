def num_of_islands(grid):
    def dfs(i, j):
        # condition checks if the current cell is out of bounds or if the current cell is water
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    if not grid:
        return 0
    
    num_of_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                num_of_islands += 1
                dfs(i, j)
    
    return num_of_islands

if __name__ == '__main__':
    grid = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    print(num_of_islands(grid)) # 1

    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    print(num_of_islands(grid)) # 3

    # generate random grid from input
    from random import randint
    grid = [[str(randint(0, 1)) for i in range(5)] for j in range(5)]
    print(num_of_islands(grid)) # random number of islands