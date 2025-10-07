# find the perimeter of an island
# input grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

def parameter(grid):
    
    # if grid is empty, return 0
    if not grid:
        return 0
    
    # get number of rows and columns
    rows, cols = len(grid), len(grid[0])
    count = 0   # initialize perimeter count
    
    # loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # if the current cell is land (1)
            if grid[i][j] == 1:
                count += 4   # add 4 sides initially
                
                # if there is land above, subtract 2 shared sides
                if i > 0 and grid[i-1][j] == 1:
                    count -= 2
                    
                # if there is land on the left, subtract 2 shared sides
                if j > 0 and grid[i][j-1] == 1:
                    count -= 2
                    
    return count   # return total perimeter

# main program
if __name__ == "__main__":
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]  # define grid
    res = parameter(grid)   # call function
    print(res)   # print the calculated perimeter
