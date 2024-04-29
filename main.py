import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    clear_screen()
    print("2048 Game:")
    for row in board:
        print("+----+----+----+----+")
        print("|", end="")
        for cell in row:
            if cell == 0:
                print("{:^4}|".format(" "), end="")
            else:
                print("{:^4}|".format(cell), end="")
        print()
    print("+----+----+----+----+")

def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

def move(board, direction):
    if direction == "W":
        board = transpose(board)
        board = move_left(board)
        board = transpose(board)
    elif direction == "S":
        board = transpose(board)
        board = move_right(board)
        board = transpose(board)
    elif direction == "A":
        board = move_left(board)
    elif direction == "D":
        board = move_right(board)
    return board

def transpose(board):
    return [list(row) for row in zip(*board)]

def move_left(board):
    for row in board:
        row[:] = merge(row)
    return board

def move_right(board):
    for row in board:
        row[:] = merge(row[::-1])[::-1]
    return board

def merge(row):
    row = [cell for cell in row if cell != 0]
    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            row[i], row[i + 1] = row[i] * 2, 0
    row = [cell for cell in row if cell != 0]
    row += [0] * (4 - len(row))
    return row

def check_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if j < 3 and board[i][j] == board[i][j + 1]:
                return False
            if i < 3 and board[i][j] == board[i + 1][j]:
                return False
    return True

def main():
    board = initialize_board()
    print_board(board)
    while True:
        direction = input("Enter W (up), A (left), S (down), D (right), or Q (quit): ").upper()
        if direction == "Q":
            print("Quitting the game.")
            break
        if direction not in ["W", "A", "S", "D"]:
            print("Invalid input! Please enter W, A, S, D, or Q.")
            continue
        board = move(board, direction)
        add_new_tile(board)
        print_board(board)
        if check_game_over(board):
            print("Game Over!")
            break

if __name__ == "__main__":
    main()
