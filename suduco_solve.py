import numpy as np

def problem_size_inp():
    try:
        inp = int(input("Please enter the size for the puzzle\n(9 for normal Sudoku):\n "))
    except KeyboardInterrupt:
        print("\nGoodbye")
        exit()
    else:
        return inp


def table_maker(inp):
    rows, cols = inp, inp
    matrix = np.zeros((rows, cols), dtype=int)
    return matrix


def problem_inp(inp):
    matrix = table_maker(inp)
    print("Enter the puzzle row by row.\nUse 0 for empty cells.\n")

    for raw in range(inp):
        while True:
            row_str = input(f"Row {raw+1} : ")
            if len(row_str) != inp or not all(ch.isdigit() for ch in row_str):
                print(f"Please enter exactly {inp} digits (0–9). Try again.")
                continue
            for col in range(inp):
                matrix[raw][col] = int(row_str[col])
            break

    return matrix


def is_valid(matrix, r, c, n, size):
    for j in range(size):
        if matrix[r][j] == n:
            return False

    for i in range(size):
        if matrix[i][c] == n:
            return False

    sub = int(size ** 0.5)
    start_r = (r // sub) * sub
    start_c = (c // sub) * sub

    for i in range(start_r, start_r + sub):
        for j in range(start_c, start_c + sub):
            if matrix[i][j] == n:
                return False

    return True


def find_empty(matrix, size):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 0:
                return i, j
    return None


def solve_sudoku(matrix, size):
    empty_position = find_empty(matrix, size)
    if not empty_position:
        return True
    r, c = empty_position

    for n in range(1, size + 1):
        if is_valid(matrix, r, c, n, size):
            matrix[r][c] = n
            if solve_sudoku(matrix, size):
                return True

            matrix[r][c] = 0
    return False

def solution(matrix, size):
    if solve_sudoku(matrix, size):
        print("\nSolved Sudoku:x")
        print(matrix)
    else:
        print("\nNo solution exists for this puzzle.")


def main():
    inp = problem_size_inp()
    matrix = problem_inp(inp)
    solution(matrix, inp)


if __name__ == "__main__":
    main()
