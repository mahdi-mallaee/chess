class Rook:
    def __init__(self, piece_position, board):
        self.piece_position = piece_position
        self.x = piece_position[0]
        self.y = piece_position[1]
        self.board_squares = board.board_squares
        self.enemy_color = 'b'
        self.get_square = board.get_square
        if board.get_square(piece_position).piece_notation[0] == 'b':
            self.enemy_color = 'w'

    def evaluate_legal_moves(self):
        legal_moves = []
        x = self.x
        y = self.y

        for i in range(1, 8):
            if 0 < x + i < 9:
                if self.get_square((x + i, y)).piece_notation == 'e':
                    legal_moves.append((x + i, y))
                else:
                    if self.get_square((x + i, y)).piece_notation[0] == self.enemy_color:
                        legal_moves.append((x + i, y))
                        break
                    else:
                        break
        for i in range(1, 8):
            if 0 < x - i < 9:
                if self.get_square((x - i, y)).piece_notation == 'e':
                    legal_moves.append((x - i, y))
                else:
                    if self.get_square((x - i, y)).piece_notation[0] == self.enemy_color:
                        legal_moves.append((x - i, y))
                        break
                    else:
                        break
        for i in range(1, 8):
            if 0 < y - i < 9:
                if self.get_square((x, y - i)).piece_notation == 'e':
                    legal_moves.append((x, y - i))
                else:
                    if self.get_square((x, y - i)).piece_notation[0] == self.enemy_color:
                        legal_moves.append((x, y - i))
                        break
                    else:
                        break

        for i in range(1, 8):
            if 0 < y + i < 9:
                if self.get_square((x, y + i)).piece_notation == 'e':
                    legal_moves.append((x, y + i))
                else:
                    if self.get_square((x, y + i)).piece_notation[0] == self.enemy_color:
                        legal_moves.append((x, y + i))
                        break
                    else:
                        break

        return legal_moves
