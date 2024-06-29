import re


# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


# Function to check if a player has won the game
def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions


# Function to check if the game is a draw
def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        max_eval = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


# Function to find the best move for the AI
def best_move(board):
    best_val = float("-inf")
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False, float("-inf"), float("inf"))
                board[i][j] = " "
                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val
    return move


# Main game loop
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human_player = "X"
    ai_player = "O"
    current_turn = "X"

    while True:
        print_board(board)
        if current_turn == human_player:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            if board[row][col] != " ":
                print("Cell already occupied! Try again.")
                continue
            board[row][col] = human_player
            if check_winner(board, human_player):
                print_board(board)
                print("Human wins!")
                break
        else:
            move = best_move(board)
            board[move[0]][move[1]] = ai_player
            if check_winner(board, ai_player):
                print_board(board)
                print("AI wins!")
                break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_turn = ai_player if current_turn == human_player else human_player


if __name__ == "__main__":
    main()
