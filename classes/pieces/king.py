class King:
    def __init__(self, piece_index, board_squares):
        self.piece_index = piece_index
        self.board_squares = board_squares
        self.color = board_squares[piece_index][0]

    def evaluate_legal_moves(self):
        legal_moves = []

        if -1 < self.piece_index - 1 < 64 and \
                self.board_squares[self.piece_index - 1][0] != self.color:
            legal_moves.append(self.piece_index - 1)
        if -1 < self.piece_index + 1 < 64 and \
                self.board_squares[self.piece_index + 1][0] != self.color:
            legal_moves.append(self.piece_index + 1)
        if -1 < self.piece_index - 8 < 64 and \
                self.board_squares[self.piece_index - 8][0] != self.color:
            legal_moves.append(self.piece_index - 8)
        if self.piece_index + 8 < 64 and \
                self.board_squares[self.piece_index + 8][0] != self.color:
            legal_moves.append(self.piece_index + 8)
        if self.piece_index + 7 < 64 and \
                self.board_squares[self.piece_index + 7][0] != self.color:
            legal_moves.append(self.piece_index + 7)
        if self.piece_index - 7 < 64 and \
                self.board_squares[self.piece_index - 7][0] != self.color:
            legal_moves.append(self.piece_index - 7)
        if self.piece_index + 9 < 64 and \
                self.board_squares[self.piece_index + 9][0] != self.color:
            legal_moves.append(self.piece_index + 9)
        if self.piece_index - 9 < 64 and \
                self.board_squares[self.piece_index - 9][0] != self.color:
            legal_moves.append(self.piece_index - 9)

        return legal_moves
