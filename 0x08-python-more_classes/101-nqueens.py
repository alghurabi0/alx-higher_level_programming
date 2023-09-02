#!/usr/bin/python3
""" solving the n queens puzzle. """
import sys


def add_sol(board, ans, n):
    """ adds a solution for the puzzle. """
    positions = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == "Q":
                positions.append([i, j])
    ans.append(positions)


def is_safe(row, col, board, n):
    """ checks if the solution is possible. """
    x = row
    y = col

    while (x >= 0):
        if board[x][y] == "Q":
            return False
        else:
            x -= 1

    x = row
    y = col

    while (y < n and x >= 0):
        if board[x][y] == "Q":
            return False
        else:
            y += 1
            x -= 1

    x = row
    y = col

    while (y >= 0 and x >= 0):
        if board[x][y] == "Q":
            return False
        else:
            y -= 1
            x -= 1
    return True


def solveNQueens(row, ans, board, n):
    """ Solves the n queens puzzle. """
    if row == n:
        add_sol(board, ans, n)
        return

    for col in range(n):
        if is_safe(row, col, board, n):
            board[row][col] = "Q"
            solveNQueens(row + 1, ans, board, n)
            board[row][col] = "."


if __name__ == "__main__":
    """ Initialization of the program. """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    board = [["." for i in range(n)] for j in range(n)]
    ans = []
    solveNQueens(0, ans, board, n)
    if ans == []:
        print("Solution does not exist")
    else:
        for a in ans:
            print(a)
