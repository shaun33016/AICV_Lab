def is_valid(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_valid(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False

def print_solution(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q",end=" ")
            else:
                print(".",end=" ")
        print()

N = int(input("Enter the number of queens: "))
board = [[0]*N for _ in range(N)]

if solve_n_queens(board, 0) == False:
    print ("Solution does not exist")
else:
    print_solution(board)
