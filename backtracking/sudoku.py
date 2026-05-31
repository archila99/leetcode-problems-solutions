def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    
def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    
    return None

def is_valid(board, row, col, num):
    # check row
    if num in board[row]:
        return False
    
    # check column 
    for r in range(9):
        if board[r][col] == num:
            return False
        
    # check 3*3 box
    start_row = (row//3) * 3
    start_col = (col//3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    
    return True

def solve(board):
    empty = find_empty(board)

    if empty is None:
        return True # Solved
    
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True
            
            board[row][col] = 0 # backtrack

    return False


board = [
    [0,0,0,3,0,0,0,0,0],
    [2,0,5,9,0,0,0,7,1],
    [0,3,0,0,0,0,5,0,9],
    [1,0,6,8,0,0,0,0,7],
    [0,0,0,4,0,7,0,0,0],
    [3,0,0,0,0,5,1,0,8],
    [5,0,1,0,0,0,0,2,0],
    [4,2,0,0,0,1,7,0,5],
    [0,0,0,0,0,9,0,0,0]
]

if __name__ == "__main__":
    if solve(board):
        print("Solved:")
        print_board(board)
    else:
        print("No solution exists.")