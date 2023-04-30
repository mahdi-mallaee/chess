class King:
    def __init__(self, piece_position, board):
        self.pos = piece_position
        self.get_square = board.get_square
        self.color = self.get_square(self.pos).color
        self.board = board

    def evaluate_legal_moves(self):
        legal_moves = []
        x = self.pos[0]
        y = self.pos[1]
        viewing_positions = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1),
                             (x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1)]

        for pos in viewing_positions:
            if 0 < pos[0] < 9 and 0 < pos[1] < 9 and self.get_square(pos).color != self.color:
                legal_moves.append(pos)

        return legal_moves

    def is_in_check(self):
        for square in self.board.board_squares:
            if square.piece_notation != 'e':
                legal_moves = square.get_legal_moves()
                for move in legal_moves:
                    s = self.get_square(move)
                    if s.piece_notation == self.color + 'k':
                        return True

        return False
