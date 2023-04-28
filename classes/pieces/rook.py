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

        for j in range(0, 4):
            for i in range(1, 8):
                check_positions = [(x + i, y), (x - i, y), (x, y + i), (x, y - i)]
                pos = check_positions[j]

                if 0 < pos[0] < 9 and 0 < pos[1] < 9:
                    if self.get_square(pos).piece_notation == 'e':
                        legal_moves.append(pos)
                    else:
                        if self.get_square(pos).piece_notation[0] == self.enemy_color:
                            legal_moves.append(pos)
                            break
                        else:
                            break

        return legal_moves
