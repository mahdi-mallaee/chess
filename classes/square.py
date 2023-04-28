import pygame
from classes.pieces.pawn import Pawn
from classes.pieces.rook import Rook
from classes.pieces.king import King
from classes.pieces.bishop import Bishop
from classes.pieces.queen import Queen
from classes.pieces.knight import Knight


class Square:
    def __init__(self, board, pos, piece_notation):
        self.board = board
        self.pos = pos
        self.piece_notation = piece_notation
        self.color = piece_notation[0]

    def get_piece_image(self):
        color = self.piece_notation[0]
        notation = self.piece_notation[1]
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
        return pygame.image.load('assets/' + color_dict[color] + '_' + notation_dict[notation] + '.png')

    def get_legal_moves(self):
        pos = self.pos
        notation = self.piece_notation[1]

        piece_dict = {
            'p': Pawn(pos, self.board),
            'r': Rook(pos, self.board),
            'k': King(pos, self.board),
            'b': Bishop(pos, self.board),
            'q': Queen(pos, self.board),
            'n': Knight(pos, self.board)
        }
        return piece_dict[notation].evaluate_legal_moves()
