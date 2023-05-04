class Bishop:
    def __init__(self, pos, board):
        self.pos = pos
        self.get_square = board.get_square
        self.color = board.get_square(pos).color

    def evaluate_legal_moves(self):
        legal_moves = []
        x = self.pos[0]
        y = self.pos[1]

        for j in range(0, 4):
            for i in range(1, 8):
                check_positions = [(x + i, y + i), (x - i, y - i), (x + i, y - i), (x - i, y + i)]
                pos = check_positions[j]

                if 0 < pos[0] < 9 and 0 < pos[1] < 9:
                    if self.get_square(pos).is_empty():
                        legal_moves.append(pos)
                    else:
                        if self.get_square(pos).color != self.color:
                            legal_moves.append(pos)
                            break
                        else:
                            break

        return legal_moves
