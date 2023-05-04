class Pawn:
    def __init__(self, pos, board):
        self.pos = pos
        self.first_move = False
        self.get_square = board.get_square
        self.color = self.get_square(self.pos).color

    def evaluate_legal_moves(self):
        x = self.pos[0]
        y = self.pos[1]
        legal_moves = []

        if self.color == 'w':
            if y == 2:
                self.first_move = True
            if 0 < y + 1 < 9 and self.get_square((x, y + 1)).is_empty():
                legal_moves.append((x, y + 1))
            if self.first_move and self.get_square((x, y + 2)).is_empty() and \
                    self.get_square((x, y + 1)).is_empty():
                legal_moves.append((x, y + 2))
            if 0 < x + 1 < 9 and 0 < y + 1 < 9 and not self.get_square((x + 1, y + 1)).is_empty() and \
                    self.get_square((x + 1, y + 1)).color != 'w':
                legal_moves.append((x + 1, y + 1))
            if 0 < x - 1 < 9 and 0 < y + 1 < 9 and not self.get_square((x - 1, y + 1)).is_empty() and \
                    self.get_square((x - 1, y + 1)).color != 'w':
                legal_moves.append((x - 1, y + 1))
        else:
            if y == 7:
                self.first_move = True
            if 0 < y - 1 < 9 and self.get_square((x, y - 1)).is_empty() and 0 < y - 1 < 9:
                legal_moves.append((x, y - 1))
            if self.first_move and self.get_square((x, y - 2)).is_empty() and \
                    self.get_square((x, y - 1)).is_empty():
                legal_moves.append((x, y - 2))
            if 0 < x - 1 < 9 and 0 < y - 1 < 9 and not self.get_square((x - 1, y - 1)).is_empty() and \
                    self.get_square((x - 1, y - 1)).color != 'b':
                legal_moves.append((x - 1, y - 1))
            if 0 < x + 1 < 9 and 0 < y - 1 < 9 and not self.get_square((x + 1, y - 1)).is_empty() and \
                    self.get_square((x + 1, y - 1)).color != 'b':
                legal_moves.append((x + 1, y - 1))

        return legal_moves
