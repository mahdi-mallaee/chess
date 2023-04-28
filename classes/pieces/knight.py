class Knight:
    def __init__(self, pos, board):
        self.pos = pos
        self.get_square = board.get_square
        self.color = self.get_square(self.pos).color

    def evaluate_legal_moves(self):
        x = self.pos[0]
        y = self.pos[1]
        legal_moves = []

        check_positions = [(x - 1, y + 2), (x + 1, y + 2), (x - 1, y - 2), (x + 1, y - 2),
                           (x - 2, y + 1), (x - 2, y - 1), (x + 2, y - 1), (x + 2, y + 1)]

        for p in check_positions:
            if 0 < p[0] < 9 and 0 < p[1] < 9 and self.get_square(p).color != self.color:
                legal_moves.append(p)

        return legal_moves
