# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

# Konstant för bräde storlek
BOARD_SIZE = 5
SHIPS = {'S': 3, 'D': 2, 'B': 4}  # Olika typer av skepp och deras längd

def create_board(size):
    return [['~' for _ in range(size)] for _ in range(size)]

def print_board(board, reveal=False):
    print("  " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        row_display = []
        for cell in row:
            row_display.append(cell if reveal or cell in ['X', 'O'] else '~')
        print(f"{i} " + " ".join(row_display))

def place_ship(board, length):
    placed = False
    while not placed:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            row, col = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - length)
            if all(board[row][col + i] == '~' for i in range(length)):
                for i in range(length):
                    board[row][col + i] = 'S'
                placed = True
        else:
            row, col = random.randint(0, BOARD_SIZE - length), random.randint(0, BOARD_SIZE - 1)
            if all(board[row + i][col] == '~' for i in range(length)):
                for i in range(length):
                    board[row + i][col] = 'S'
                placed = True

def place_all_ships(board):
    for ship, length in SHIPS.items():
        place_ship(board, length)

def player_turn(board):
    print("\nDin tur! Använd formatet rad kolumn (t.ex. 2 3)")
    try:
        row, col = map(int, input("Ange rad och kolumn: ").split())
        if board[row][col] == 'S':
            board[row][col] = 'X'
            print("Träff!")
            return True
        elif board[row][col] == '~':
            board[row][col] = 'O'
            print("Miss!")
            return False
        else:
            print("Redan använt! Försök igen.")
            return player_turn(board)
    except (ValueError, IndexError):
        print("Felaktig inmatning! Försök igen.")
        return player_turn(board)

def computer_turn(board):
    row, col = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
    while board[row][col] in ['X', 'O']:
        row, col = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
    if board[row][col] == 'S':
        board[row][col] = 'X'
        print(f"Datorn träffade på {row} {col}!")
        return True
    else:
        board[row][col] = 'O'
        print(f"Datorn missade på {row} {col}.")
        return False

def check_win(board):
    return all(cell != 'S' for row in board for cell in row)

def main():
    print("Välkommen till Battleship!")
    player_board = create_board(BOARD_SIZE)
    computer_board = create_board(BOARD_SIZE)
    place_all_ships(player_board)
    place_all_ships(computer_board)

    while True:
        print("\nDitt bräde:")
        print_board(player_board, reveal=True)
        print("\nDatorns bräde:")
        print_board(computer_board)

        if player_turn(computer_board):
            if check_win(computer_board):
                print("Grattis! Du har besegrat datorn!")
                break

        if computer_turn(player_board):
            if check_win(player_board):
                print("Datorn vann! Bättre lycka nästa gång!")
                break

if __name__ == "__main__":
    main()