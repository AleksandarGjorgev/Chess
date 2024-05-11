class BlindChess:
    def __init__(self):
        self.board = self.setup_board()
        self.turn = 'w'  # 'w' for white's turn, 'b' for black's turn

    def setup_board(self):
        # Simplified board setup, normally you'd have all pieces
        board = [['  ' for _ in range(8)] for _ in range(8)]
        board[6] = ['wP' for _ in range(8)]  # White pawns
        board[1] = ['bP' for _ in range(8)]  # Black pawns
        return board

    def print_board(self):  # For debugging, in a real blind game you wouldn't print the board
        for row in self.board:
            print(' '.join(row))
        print()

    def move(self, start, end):
        start_row, start_col = self.pos_to_index(start)
        end_row, end_col = self.pos_to_index(end)
        piece = self.board[start_row][start_col]
        self.board[start_row][start_col] = '  '
        self.board[end_row][end_col] = piece
        self.turn = 'b' if self.turn == 'w' else 'w'

    def pos_to_index(self, pos):
        col_to_index = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        row = 8 - int(pos[1])  # Convert chess row to 0-indexed row
        col = col_to_index[pos[0].lower()]
        return row, col

# Example usage
game = BlindChess()
game.print_board()  # For debugging
game.move('kn3', 'e7')
game.print_board()  # For debugging