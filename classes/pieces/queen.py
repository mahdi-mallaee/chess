class Queen:
    def __init__(self, pos, board):
        self.pos = pos
        self.get_square = board.get_square
        self.color = board.get_square(pos).color

    def evaluate_legal_moves(self):
        x = self.pos[0]
        y = self.pos[1]
        legal_moves = []

        for j in range(0, 8):
            for i in range(1, 8):
                check_positions = [(x + i, y + i), (x - i, y - i), (x + i, y - i), (x - i, y + i),
                                   (x + i, y), (x - i, y), (x, y + i), (x, y - i)]
                pos = check_positions[j]

                if 0 < pos[0] < 9 and 0 < pos[1] < 9:
                    if self.get_square(pos).piece_notation == 'e':
                        legal_moves.append(pos)
                    else:
                        if self.get_square(pos).color != self.color and self.get_square(pos).color != 'e':
                            legal_moves.append(pos)
                            break
                        else:
                            break

        return legal_moves
