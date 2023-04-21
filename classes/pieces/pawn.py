class Pawn:
    def __init__(self, piece_index, board_squares):
        self.first_move = False
        self.board_squares = board_squares
        self.color = board_squares[piece_index][0]
        self.piece_index = piece_index

    def evaluate_legal_moves(self):
        legal_moves = []
        if self.color == 'w':
            if int((self.piece_index + 1) / 8) == 6:
                self.first_move = True
            if self.board_squares[self.piece_index - 8] == 'e':
                legal_moves.append(self.piece_index - 8)
            if self.first_move and self.board_squares[self.piece_index - 16] == 'e':
                legal_moves.append(self.piece_index - 16)
            if self.board_squares[self.piece_index - 7] != 'e' and self.board_squares[self.piece_index - 7][0] != 'w':
                legal_moves.append(self.piece_index - 7)
            if self.board_squares[self.piece_index - 9] != 'e' and self.board_squares[self.piece_index - 9][0] != 'w':
                legal_moves.append(self.piece_index - 9)
        else:
            if int((self.piece_index + 1) / 8) == 1:
                self.first_move = True
            if self.board_squares[self.piece_index + 8] == 'e':
                legal_moves.append(self.piece_index + 8)
            if self.first_move and self.board_squares[self.piece_index + 16] == 'e':
                legal_moves.append(self.piece_index + 16)
            if self.board_squares[self.piece_index + 7] != 'e' and self.board_squares[self.piece_index + 7][0] != 'b':
                legal_moves.append(self.piece_index + 7)
            if self.board_squares[self.piece_index + 9] != 'e' and self.board_squares[self.piece_index + 9][0] != 'b':
                legal_moves.append(self.piece_index + 9)

        return legal_moves
