# https://leetcode.com/problems/island-perimeter/description/
def islandPerimeter(grid: list[list[int]]) -> int:
    perimeter = 0
    for row_index in range(len(grid)):
        for column_index in range(len(grid[row_index])):
            if grid[row_index][column_index] == 1:
                if grid[row_index][column_index-1] == 0 or column_index == 0:
                    perimeter+=1
                if column_index == len(grid[row_index])-1 or grid[row_index][column_index+1] == 0:
                    perimeter+=1
                if grid[row_index-1][column_index] == 0 or row_index == 0:
                    perimeter+=1
                if row_index == len(grid)-1 or grid[row_index+1][column_index] == 0:
                    perimeter+=1
    return perimeter

print(islandPerimeter([[0,1,0,0],
                       [1,1,1,0],
                       [0,1,0,0],
                       [1,1,0,0]])
      ) # 16
print(islandPerimeter([[1]]) ) # 4
print(islandPerimeter([[1,0]]) ) # 4
print(islandPerimeter([[1,1]]) ) # 6
print(islandPerimeter([[1,1],[1,1]]) ) # 8
print(islandPerimeter([[1,1,1],[1,1,1]]) ) # 10
print(islandPerimeter([[1,1,1,1],[1,1,1,1]]) ) # 12
print(islandPerimeter([[1,1,1,1,1],[1,1,1,1,1]]) ) # 14
