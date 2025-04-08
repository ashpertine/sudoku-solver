#make sudoku solver
import board

def check_num(num, unavail_num):   
    if num in unavail_num:
        return False
    else:
        return True

def get_sub_grid (grid, row_i, col_i):
    sub_grid = []
    starting_col_i = col_i
    starting_row_i = row_i
    #col_index is at the start
    if col_i == 0 and row_i == 0:
        for row_iterate in range(3):
            sub_grid.extend([grid[row_iterate][i] for i in range(col_i, col_i+3)])
    else:
        if col_i in (1, 4, 7):
            starting_col_i = col_i - 1
        elif col_i in (2, 5, 8):
            starting_col_i  = col_i - 2

        if row_i in (1, 4, 7):
            starting_row_i = row_i -1
        elif row_i in (2, 5, 8):
            starting_row_i = row_i - 2

        for row_iterate in range(3):
            sub_grid.extend([grid[starting_row_i + row_iterate][i] for i in range(starting_col_i, starting_col_i+3)])

    return sub_grid

def get_unavailable_num(grid, row_i, col_i):
    unavailable_numbers_row = [x for x in grid[row_i] if x != 0]
    unavailable_numbers_col = []
    for i in range(len(grid)):
        if grid[i][col_i] != 0:
            unavailable_numbers_col.append(grid[i][col_i])
    
    unavailable_numbers_sub_grid = get_sub_grid(grid, row_i, col_i)
    
    return list(set(unavailable_numbers_col + unavailable_numbers_row + unavailable_numbers_sub_grid))

def solve(grid, row_i, col_i):
    #if the code reaches end of the grid
    if row_i >= len(grid):
        return True
    #if the code reaches end of a row
    if col_i >= len(grid[row_i]):
        return solve(grid, row_i+1, 0)
    
    #if the current cell is already filled
    if grid[row_i][col_i] != 0:
        return solve(grid, row_i, col_i+1)

    unavailable_numbers =  get_unavailable_num(grid, row_i, col_i)
    
    for num in range(1, 10):
        if check_num(num, unavailable_numbers):
            grid[row_i][col_i] = num
            if solve(grid, row_i, col_i+1): #if solution is found: return true to indicate success
                return True
            #solution not found
            grid[row_i][col_i] = 0

    #iterate through 1 to 9: not solution found
    return False


if __name__ == "__main__":
    grid = board.grid3
    solve(grid, 0, 0)
    for i in grid:
        print(i, end='\n')