import random

def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()

def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def ai_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)  # AI randomly selects an empty spot

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Player
    ai_player = "O"  # AI
    print("🎮 Welcome to Tic-Tac-Toe (Player vs AI)")
    print_board(board)

    while True:
        if current_player == "X":  # Player's turn
            try:
                row = int(input(f"Player {current_player}, enter row (0-2): "))
                col = int(input(f"Player {current_player}, enter col (0-2): "))

                if board[row][col] != " ":
                    print("❌ Spot already taken. Try again.")
                    continue

                board[row][col] = current_player
                print_board(board)

                if check_winner(board, current_player):
                    print(f"🎉 Player {current_player} wins!")
                    break

                if is_full(board):
                    print("🤝 It's a draw!")
                    break

                current_player = ai_player  # Switch to AI
            except (ValueError, IndexError):
                print("❌ Invalid input. Please enter row and col as numbers between 0 and 2.")
        else:  # AI's turn
            print(f"AI ({ai_player}) is making a move...")
            row, col = ai_move(board)
            board[row][col] = ai_player
            print_board(board)

            if check_winner(board, ai_player):
                print(f"🎉 AI ({ai_player}) wins!")
                break

            if is_full(board):
                print("🤝 It's a draw!")
                break

            current_player = "X"  # Switch back to player

if __name__ == "__main__":
    tic_tac_toe()
