def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    lines = (board +
            [[board[i][j] for i in range(3)] for j in range(3)] +
            [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]])

    for line in lines:
        if len(set(line)) == 1 and line[0] != " ":
            return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    total_moves = 0

    while not check_winner(board) and total_moves < 9:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = player
                total_moves += 1
                player = "O" if player == "X" else "X"
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print_board(board)
    if check_winner(board):
        print("Player " + player + " wins!")
    else:
        print("It's a tie!")

tic_tac_toe()
