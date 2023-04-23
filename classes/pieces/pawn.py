class Pawn:
    def __init__(self, piece_position, board):
        self.x = piece_position[0]
        self.y = piece_position[1]
        self.pos = (self.x, self.y)
        self.first_move = False
        self.board_squares = board.board_squares
        self.get_square = board.get_square
        self.color = self.get_square(self.pos).piece_notation[0]

    def evaluate_legal_moves(self):
        x = self.x
        y = self.y
        legal_moves = []

        if self.color == 'w':
            if y == 2:
                self.first_move = True
            if 0 < y + 1 < 9 and self.get_square((x, y + 1)).piece_notation == 'e':
                legal_moves.append((x, y + 1))
            if self.first_move and self.get_square((x, y + 2)).piece_notation == 'e' and \
                    self.get_square((x, y + 1)).piece_notation == 'e':
                legal_moves.append((x, y + 2))
            if 0 < x + 1 < 9 and 0 < y + 1 < 9 and self.get_square((x + 1, y + 1)).piece_notation != 'e' and \
                    self.get_square((x + 1, y + 1)).piece_notation[0] != 'w':
                legal_moves.append((x + 1, y + 1))
            if 0 < x - 1 < 9 and 0 < y + 1 < 9 and self.get_square((x - 1, y + 1)).piece_notation != 'e' and \
                    self.get_square((x - 1, y + 1)).piece_notation[0] != 'w':
                legal_moves.append((x - 1, y + 1))
        else:
            if y == 7:
                self.first_move = True
            if 0 < y - 1 < 9 and self.get_square((x, y - 1)).piece_notation == 'e' and 0 < y - 1 < 9:
                legal_moves.append((x, y - 1))
            if self.first_move and self.get_square((x, y - 2)).piece_notation == 'e' and \
                    self.get_square((x, y - 1)).piece_notation == 'e':
                legal_moves.append((x, y - 2))
            if 0 < x - 1 < 9 and 0 < y - 1 < 9 and self.get_square((x - 1, y - 1)).piece_notation != 'e' and \
                    self.get_square((x - 1, y - 1)).piece_notation[0] != 'b':
                legal_moves.append((x - 1, y - 1))
            if 0 < x + 1 < 9 and 0 < y - 1 < 9 and self.get_square((x + 1, y - 1)).piece_notation != 'e' and \
                    self.get_square((x + 1, y - 1)).piece_notation[0] != 'b':
                legal_moves.append((x + 1, y - 1))

        return legal_moves
