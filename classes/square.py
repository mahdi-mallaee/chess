class Square:
    def __init__(self, square_position, piece_notation):
        self.x = square_position[0]
        self.y = square_position[1]
        self.pos = (self.x, self.y)
        self.piece_notation = piece_notation
