"""
Given an integer n, the task is to find all distinct solutions to the n-queens problem, 
where n queens are placed on an n * n chessboard such that no two queens can attack each other.
"""

def isSafe(board, currRow, currCol):
    for i in range(len(board)):
        placedRow = board[i]
        placedCol = i + 1

        # Check diagonals
        if abs(placedRow - currRow) == abs(placedCol - currCol):
            return False

    return True


def nQueenUtil(col, n, board, res, visited):
    if col > n:
        res.append(board.copy())
        return

    for row in range(1, n + 1):
        if not visited[row]:
            if isSafe(board, row, col):
                visited[row] = True
                board.append(row)

                nQueenUtil(col + 1, n, board, res, visited)

                board.pop()
                visited[row] = False


def nQueen(n):
    res = []
    board = []
    visited = [False] * (n + 1)
    nQueenUtil(1, n, board, res, visited)
    return res


if __name__ == "__main__":
    n = 4
    res = nQueen(n)
    for row in res:
        print(row)
