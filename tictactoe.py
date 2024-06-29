import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize empty board
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Display the board with numbers for reference
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # Returns a list of indices of empty spots on the board
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # If the move is valid, place the letter on the board
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Top-left to bottom-right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Top-right to bottom-left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def minimax(board, depth, maximizing_player):
    if board.current_winner == 'X':
        return -1
    elif board.current_winner == 'O':
        return 1
    elif not board.empty_squares():
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.available_moves():
            board.make_move(move, 'O')
            eval = minimax(board, depth + 1, False)
            board.board[move] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.available_moves():
            board.make_move(move, 'X')
            eval = minimax(board, depth + 1, True)
            board.board[move] = ' '
            min_eval = min(min_eval, eval)
        return min_eval


def get_ai_move(board):
    # Implementing the minimax algorithm to get the optimal move for AI
    best_move = None
    best_score = float('-inf')
    for move in board.available_moves():
        board.make_move(move, 'O')
        score = minimax(board, 0, False)
        board.board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def main():
    game = TicTacToe()
    game.print_board_nums()
    print("To make a move, enter a number from 0-8 to place your X on the board.")

    while game.empty_squares():
        # Human's turn
        human_move = None
        while human_move not in game.available_moves():
            human_move = int(input("Enter your move (0-8): "))
        game.make_move(human_move, 'X')
        game.print_board()

        # Check for human win or draw
        if game.current_winner == 'X':
            print("Congratulations! You win!")
            break
        elif not game.empty_squares():
            print("It's a draw!")
            break

        # AI's turn
        ai_move = get_ai_move(game)
        game.make_move(ai_move, 'O')
        print(f"AI placed an O on square {ai_move}:")
        game.print_board()

        # Check for AI win or draw
        if game.current_winner == 'O':
            print("AI wins! Better luck next time.")
            break
        elif not game.empty_squares():
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()
