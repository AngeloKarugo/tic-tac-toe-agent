# Tic-Tac-Toe Game with Minimax AI Agent

# Initialize the board as a 3x3 grid
def init_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Print the board in a readable format
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Check if the board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Get available moves on the board
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

# Minimax algorithm to determine the best move
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 10 - depth
    if check_winner(board, "X"):
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for (i, j) in get_available_moves(board):
            board[i][j] = "O"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for (i, j) in get_available_moves(board):
            board[i][j] = "X"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(best_score, score)
        return best_score

# Find the best move for the AI agent
def find_best_move(board):
    best_move = None
    best_score = float("-inf")
    for (i, j) in get_available_moves(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

# Main game loop
def play_game():
    board = init_board()
    print("Welcome to Tic-Tac-Toe! You are 'X'. AI is 'O'.")
    print_board(board)

    while True:
        # User move
        user_move = input("Enter your move as row,col (e.g., 1,2): ")
        try:
            row, col = map(int, user_move.split(","))
            if board[row][col] != " ":
                print("Cell is already occupied. Try again.")
                continue
            board[row][col] = "X"
        except (ValueError, IndexError):
            print("Invalid input. Use the format row,col with numbers between 0 and 2.")
            continue

        print_board(board)

        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making its move...")
        ai_move = find_best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = "O"
            print_board(board)

        if check_winner(board, "O"):
            print("AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
