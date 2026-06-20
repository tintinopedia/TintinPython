# Noughts and Crosses (Tic Tac Toe)

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def show_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def check_winner():
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combos:
        a, b, c = combo
        if board[a] == board[b] == board[c]:
            return board[a]
    return None

current_player = "X"
for turn in range(9):
    show_board()
    pos = int(input(f"Player {current_player}, choose a position (1-9): "))
    if board[pos - 1] in ("X", "O"):
        print("That position is already taken. Try again.")
        continue
    board[pos - 1] = current_player

    winner = check_winner()
    if winner:
        show_board()
        print(f"Player {winner} wins!! 🎉")
        break

    current_player = "O" if current_player == "X" else "X"
else:
    show_board()
    print("It's a draw!")
