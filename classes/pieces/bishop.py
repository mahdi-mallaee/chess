class Bishop:
    def __init__(self, pos, board):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.board_squares = board.board_squares
        self.get_square = board.get_square
        self.notation = board.get_square(pos).piece_notation
        self.enemy_color = 'b'
        if self.notation[0] == 'b':
            self.enemy_color = 'w'

    def evaluate_legal_moves(self):
        legal_moves = []
        x = self.x
        y = self.y

        for j in range(0, 4):
            for i in range(1, 8):
                check_positions = [(x + i, y + i), (x - i, y - i), (x + i, y - i), (x - i, y + i)]
                pos = check_positions[j]

                if 0 < pos[0] < 9 and 0 < pos[1] < 9:
                    print(pos, self.get_square(pos).piece_notation)
                    if self.get_square(pos).piece_notation == 'e':
                        legal_moves.append(pos)
                    else:
                        if self.get_square(pos).piece_notation[0] == self.enemy_color:
                            legal_moves.append(pos)
                            break
                        else:
                            break

        return legal_moves
