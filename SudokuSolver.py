from Sudoku import ReturnSudoku
import numpy as np
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


# Check if n in row
# Returns true if number is not present
def check_row(n,i,sudoku):
    if n in sudoku[i]:
        return False
    return True


# Check if n in column
# Returns true if number is not present
def check_column(n,j,sudoku):
    if n in [row[j] for row in sudoku]:
        return False
    return True

# Check if n in quadrant
# Returns true if number is not present
def check_quadrant(n,i,j,sudoku):
    i_rest = i-(i % 3)
    j_rest = j-(j % 3)
    if n in sudoku[i_rest:i_rest+3,j_rest:j_rest+3]:
        return False
    return True


# Returns true if number can be placed
def check_valid(n,i,j,sudoku):
    if check_column(n,j,sudoku):
        if check_row(n,i,sudoku):
            if check_quadrant(n,i,j,sudoku):
                return True
    return False

# Checks where the next empty slot is
def find_empty(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i,j)
    return False


# Solve sudoku with depth-first search
# Return True if sudoku is solved
def solve_sudoku(sudoku):
    next_empty = find_empty(sudoku)
    if not next_empty:
        return True
    row,col = next_empty

    for n in range(1,10):
        if check_valid(n,row,col,sudoku):
            sudoku[row][col] = n

            if solve_sudoku(sudoku):
                return True

            sudoku[row][col] = 0
    return None

# Function to print the sudoku
def print_sudoku(solved):
    for row in solved:
        print(row)

# Validates if the sudoku has indeed been solved
def validate(sudoku):
    sorted_list = np.arange(1,10)
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if not np.array_equal(np.sort(sudoku[i]),sorted_list):
                return False
            if not np.array_equal(np.sort([row[j] for row in sudoku]),sorted_list):
                return False
            i_rest = i-(i % 3)
            j_rest = j-(j % 3)
            if not np.array_equal(np.sort(sudoku[i_rest:i_rest+3,j_rest:j_rest+3].ravel()),sorted_list):
                return False
    return True

def main():
    sudoku = ReturnSudoku()
    solve_sudoku(sudoku)
    if sudoku is not None:
        if validate(sudoku):
            print_sudoku(sudoku)
            return 0
        else:
            print('Did not find a solution')
            return 1
    print('Not a valid sudoku!')
    return 1



if __name__ == '__main__':
    main()
