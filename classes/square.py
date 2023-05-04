import pygame
from classes.pieces.pawn import Pawn
from classes.pieces.rook import Rook
from classes.pieces.king import King
from classes.pieces.bishop import Bishop
from classes.pieces.queen import Queen
from classes.pieces.knight import Knight


class Square:
    def __init__(self, board, pos, notation, color):
        self.board = board
        self.pos = pos
        self.notation = notation
        self.color = color

    def get_piece_image(self):
        color_dict = {
            'b': 'black',
            'w': 'white'
        }
        notation_dict = {
            'r': 'rook',
            'n': 'knight',
            'b': 'bishop',
            'q': 'queen',
            'k': 'king',
            'p': 'pawn'
        }
        return pygame.image.load('assets/' + color_dict[self.color] + '_' + notation_dict[self.notation] + '.png')

    def get_legal_moves(self):
        pos = self.pos

        piece_dict = {
            'p': Pawn(pos, self.board),
            'r': Rook(pos, self.board),
            'k': King(pos, self.board),
            'b': Bishop(pos, self.board),
            'q': Queen(pos, self.board),
            'n': Knight(pos, self.board)
        }
        return piece_dict[self.notation].evaluate_legal_moves()

    def is_in_check(self):
        pos = self.board.get_squares_by_notation('k', self.color)[0].pos
        king = King(pos, self.board)
        return king.is_in_check()

    def is_empty(self):
        if self.notation == 'e':
            return True
        else:
            return False
