from classes.square import Square


class EBoard:
    def __init__(self, board_squares, turn_color):
        self.board_squares = self.initial_board_squares(board_squares)
        self.turn_color = turn_color

    def initial_board_squares(self, squares):
        board_squares = []

        for square in squares:
            new_square = Square(self, square.pos, square.piece_notation)
            board_squares.append(new_square)

        return board_squares

    def get_square(self, piece_position):
        for square in self.board_squares:
            if square.pos == piece_position:
                return square

    def get_squares_by_notation(self, notation):
        squares = []
        for s in self.board_squares:
            if s.piece_notation == notation:
                squares.append(s)
        return squares

    def is_in_check(self):
        square = self.get_squares_by_notation(self.turn_color + 'k')[0]
        return square.is_in_check()

    def move_piece(self, i_pos, f_pos):
        piece = self.get_square(i_pos)
        square = self.get_square(f_pos)
        notation = piece.piece_notation
        piece.piece_notation = 'e'
        square.piece_notation = notation
        square.color = notation[0]
        piece.color = 'e'
