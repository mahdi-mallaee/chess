import pygame
from classes.pieces.pawn import Pawn
from classes.pieces.rook import Rook
from classes.pieces.king import King


class Square:
    def __init__(self, board, square_position, piece_notation):
        self.board = board
        self.x = square_position[0]
        self.y = square_position[1]
        self.pos = (self.x, self.y)
        self.piece_notation = piece_notation

    def get_piece_image(self):
        color = "white"
        notation = self.piece_notation[1]
        if self.piece_notation[0] == 'b':
            color = 'black'

        if notation == 'r':
            piece_image = pygame.image.load('assets/' + color + '_rook.png')
        elif notation == 'n':
            piece_image = pygame.image.load('assets/' + color + '_knight.png')
        elif notation == 'b':
            piece_image = pygame.image.load('assets/' + color + '_bishop.png')
        elif notation == 'q':
            piece_image = pygame.image.load('assets/' + color + '_queen.png')
        elif notation == 'k':
            piece_image = pygame.image.load('assets/' + color + '_king.png')
        elif notation == 'p':
            piece_image = pygame.image.load('assets/' + color + '_pawn.png')

        return piece_image

    def get_legal_moves(self):
        pos = self.pos
        if self.piece_notation[1] == 'p':
            pawn = Pawn(pos, self.board)
            return pawn.evaluate_legal_moves()
        elif self.piece_notation[1] == 'r':
            rook = Rook(pos, self.board)
            return rook.evaluate_legal_moves()
        elif self.piece_notation[1] == 'k':
            king = King(pos, self.board)
            return king.evaluate_legal_moves()
