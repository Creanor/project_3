# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

# Konstant för bräde storlek och skeppstyper
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

def place_ship_manually(board, ship_type, length):
    print(f"\nPlacera skeppet '{ship_type}' som är {length} rutor långt.")
    placed = False
    while not placed:
        try:
            row, col = map(int, input("Ange startposition för skeppet (rad kolumn): ").split())
            direction = input("Ange riktning (h för horisontell, v för vertikal): ").lower()
            if direction == 'h' and col + length <= BOARD_SIZE:
                if all(board[row][col + i] == '~' for i in range(length)):
                    for i in range(length):
                        board[row][col + i] = ship_type
                    placed = True
                else:
                    print("Platsen är redan upptagen. Försök igen.")
            elif direction == 'v' and row + length <= BOARD_SIZE:
                if all(board[row + i][col] == '~' for i in range(length)):
                    for i in range(length):
                        board[row + i][col] = ship_type
                    placed = True
                else:
                    print("Platsen är redan upptagen. Försök igen.")
            else:
                print("Ogiltig position eller riktning. Försök igen.")
        except (ValueError, IndexError):
            print("Felaktig inmatning! Försök igen.")

def place_all_ships_manually(board):
    for ship, length in SHIPS.items():
        print_board(board, reveal=True)
        place_ship_manually(board, ship, length)

def place_ship_computer(board, length):
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

def place_all_ships_computer(board):
    for ship, length in SHIPS.items():
        place_ship_computer(board, length)

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
    if board[row][col] in SHIPS.keys():
        board[row][col] = 'X'
        print(f"Datorn träffade på {row} {col}!")
        return True
    else:
        board[row][col] = 'O'
        print(f"Datorn missade på {row} {col}.")
        return False

def check_win(board):
    return all(cell not in SHIPS.keys() for row in board for cell in row)

def main():
    print("Välkommen till Battleship!")
    player_board = create_board(BOARD_SIZE)
    computer_board = create_board(BOARD_SIZE)
    
    # Placera spelarnas skepp
    place_all_ships_manually(player_board)
    place_all_ships_computer(computer_board)

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