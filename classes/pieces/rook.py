class Rook:
    def __init__(self, piece_index, board_squares):
        self.piece_index = piece_index
        self.board_squares = board_squares
        self.enemy_color = 'b'
        if board_squares[piece_index][0] == 'b':
            self.enemy_color = 'w'

    def evaluate_legal_moves(self):
        legal_moves = []
        x_pos = ((self.piece_index / 8) - int(self.piece_index / 8)) * 8
        x_pos = int(x_pos)

        for x in range(1, 8 - x_pos):
            if -1 < self.piece_index + x < 64:
                if self.board_squares[self.piece_index + x] == 'e':
                    legal_moves.append(self.piece_index + x)
                else:
                    if self.board_squares[self.piece_index + x][0] == self.enemy_color:
                        legal_moves.append(self.piece_index + x)
                        break
                    else:
                        break
        for x in range(1, x_pos + 1):
            if -1 < self.piece_index - x < 64:
                if self.board_squares[self.piece_index - x] == 'e':
                    legal_moves.append(self.piece_index - x)
                else:
                    if self.board_squares[self.piece_index - x][0] == self.enemy_color:
                        legal_moves.append(self.piece_index - x)
                        break
                    else:
                        break
        for i in range(1, 8):
            y = i * 8
            if -1 < self.piece_index - y < 64:
                if self.board_squares[self.piece_index - y] == 'e':
                    legal_moves.append(self.piece_index - y)
                else:
                    if self.board_squares[self.piece_index - y][0] == self.enemy_color:
                        legal_moves.append(self.piece_index - y)
                        break
                    else:
                        break
        for i in range(1, 8):
            y = i * 8
            if -1 < self.piece_index + y < 64:
                if self.board_squares[self.piece_index + y] == 'e':
                    legal_moves.append(self.piece_index + y)
                else:
                    if self.board_squares[self.piece_index + y][0] == self.enemy_color:
                        legal_moves.append(self.piece_index + y)
                        break
                    else:
                        break

        return legal_moves
