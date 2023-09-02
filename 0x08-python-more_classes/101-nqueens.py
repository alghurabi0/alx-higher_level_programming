#!/usr/bin/python3
""" solving the n queens puzzle. """
import sys


def foundIt(chess, solutions, n):
    """ adds a solution for the puzzle. """
    positions = []
    for i in range(n):
        for j in range(n):
            if chess[i][j] == "Q":
                positions.append([i, j])
    solutions.append(positions)


def check(row, col, chess, n):
    """ checks if the solution is possible. """
    x = row
    y = col

    while (x >= 0):
        if chess[x][y] == "Q":
            return False
        else:
            x -= 1

    x = row
    y = col

    while (y < n and x >= 0):
        if chess[x][y] == "Q":
            return False
        else:
            y += 1
            x -= 1

    x = row
    y = col

    while (y >= 0 and x >= 0):
        if chess[x][y] == "Q":
            return False
        else:
            y -= 1
            x -= 1
    return True


def solve(row, solutions, chess, n):
    """ Solves the n queens puzzle. """
    if row == n:
        foundIt(chess, solutions, n)
        return

    for col in range(n):
        if check(row, col, chess, n):
            chess[row][col] = "Q"
            solve(row + 1, solutions, chess, n)
            chess[row][col] = "."


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

    chess = [["." for i in range(n)] for j in range(n)]
    solutions = []
    solve(0, solutions, chess, n)
    if solutions == []:
        print("0")
    else:
        for a in solutions:
            print(a)
