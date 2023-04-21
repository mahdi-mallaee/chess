import pygame
from classes.pieces.pawn import Pawn
from classes.pieces.rook import Rook
from classes.pieces.king import King


def translate_board_string(board_string):
    board_string = str(board_string)
    rows = board_string.split("/")
    board = []
    for row in rows:
        squares = row.split('-')
        for square in squares:
            if square.isnumeric():
                s = int(square)
                for i in range(0, s):
                    board.append('e')
            else:
                board.append(square)
    return board


COLOR_ODD = (100, 100, 100)
COLOR_EVEN = (200, 200, 200)


def get_piece_image(piece_string):
    piece_image = pygame.image.load('assets/white_king.png')
    if piece_string == 'wr':
        piece_image = pygame.image.load('assets/white_rook.png')
    elif piece_string == 'wn':
        piece_image = pygame.image.load('assets/white_knight.png')
    elif piece_string == 'wb':
        piece_image = pygame.image.load('assets/white_bishop.png')
    elif piece_string == 'wq':
        piece_image = pygame.image.load('assets/white_queen.png')
    elif piece_string == 'wk':
        piece_image = pygame.image.load('assets/white_king.png')
    elif piece_string == 'wp':
        piece_image = pygame.image.load('assets/white_pawn.png')
    elif piece_string == 'br':
        piece_image = pygame.image.load('assets/black_rook.png')
    elif piece_string == 'bb':
        piece_image = pygame.image.load('assets/black_bishop.png')
    elif piece_string == 'bn':
        piece_image = pygame.image.load('assets/black_knight.png')
    elif piece_string == 'bk':
        piece_image = pygame.image.load('assets/black_king.png')
    elif piece_string == 'bq':
        piece_image = pygame.image.load('assets/black_queen.png')
    elif piece_string == 'bp':
        piece_image = pygame.image.load('assets/black_pawn.png')
    return piece_image


class Board:
    def __init__(self, width, screen):
        self.screen = screen
        self.width = width
        self.square_width = width / 8
        self.initial_board_string = "br-bn-bb-bq-bk-bb-bn-br/bp-bp-bp-bp-bp-bp-bp-bp/8/8/8/8/" \
                                    "wp-wp-wp-wp-wp-wp-wp-wp/wr-wn-wb-wq-wk-wb-wn-wr"
        self.board_squares = translate_board_string(self.initial_board_string)
        self.selected_square_index = -1
        self.selected_piece_index = -1
        self.legal_moves_of_selected_piece = []

    def initial_board(self):
        self.board_squares = translate_board_string(self.initial_board_string)
        self.draw_board()

    def handle_click_on_board(self, mouse_x, mouse_y):
        x = int(mouse_x / self.square_width)
        y = int(mouse_y / self.square_width)
        square_index = x + (y * 8)
        if self.selected_piece_index == -1:
            if self.board_squares[square_index] != 'e':
                self.selected_piece_index = square_index
                self.set_legal_moves()
            self.draw_board()
        else:
            self.selected_square_index = square_index
            if self.legal_moves_of_selected_piece.count(square_index) == 1:
                self.move_piece()

            self.selected_square_index = -1
            self.selected_piece_index = -1
            self.legal_moves_of_selected_piece = []
            self.draw_board()

    def set_legal_moves(self):
        square_index = self.selected_piece_index
        if self.board_squares[square_index][1] == 'p':
            pawn = Pawn(square_index, self.board_squares)
            self.legal_moves_of_selected_piece = pawn.evaluate_legal_moves()
        elif self.board_squares[square_index][1] == 'r':
            rook = Rook(square_index, self.board_squares)
            self.legal_moves_of_selected_piece = rook.evaluate_legal_moves()
        elif self.board_squares[square_index][1] == 'k':
            king = King(square_index, self.board_squares)
            self.legal_moves_of_selected_piece = king.evaluate_legal_moves()

    def move_piece(self):
        piece_notation = self.board_squares[self.selected_piece_index]
        self.board_squares[self.selected_piece_index] = 'e'
        self.board_squares[self.selected_square_index] = piece_notation

    def draw_board(self):
        for y in range(0, 8):
            for x in range(0, 8):
                square_index = x + (y * 8)

                if (x + y) % 2 == 1:
                    color = COLOR_ODD
                else:
                    color = COLOR_EVEN

                square_rect = pygame.draw.rect(self.screen, color, (
                    x * self.square_width, y * self.square_width, self.square_width, self.square_width))

                if self.board_squares[square_index] != "e":
                    image = get_piece_image(self.board_squares[square_index])
                    image = pygame.transform.scale(image, (self.square_width - 10, self.square_width - 10))
                    image_rect = image.get_rect()
                    image_rect.center = square_rect.center
                    self.screen.blit(image, image_rect)

                if self.legal_moves_of_selected_piece.count(square_index) == 1:
                    pygame.draw.circle(self.screen, "red", square_rect.center, 20)

                pygame.display.flip()
