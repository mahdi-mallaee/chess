import pygame
from classes.pieces.pawn import Pawn
from classes.pieces.rook import Rook
from classes.pieces.king import King
from classes.square import Square


def translate_board_string(board_string):
    board_string = str(board_string)
    rows = board_string.split("/")
    board = []
    y = 0
    for row in rows:
        y += 1
        x = 0
        notations = row.split('-')
        for notation in notations:
            if notation.isnumeric():
                empty_squares_count = int(notation)
                for i in range(0, empty_squares_count):
                    x += 1
                    square = Square((x, y), 'e')
                    board.append(square)
            else:
                x += 1
                square = Square((x, y), notation)
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
        self.initial_board_string = "wr-wn-wb-wq-wk-wb-wn-wr/wp-wp-wp-wp-wp-wp-wp-wp/8/8/8/8/" \
                                    "bp-bp-bp-bp-bp-bp-bp-bp/br-bn-bb-bq-bk-bb-bn-br"
        self.board_squares = translate_board_string(self.initial_board_string)
        self.selected_square_position = (0, 0)
        self.selected_piece_position = (0, 0)
        self.legal_moves_of_selected_piece = []

    def initial_board(self):
        self.board_squares = translate_board_string(self.initial_board_string)
        self.draw_board()

    def get_square(self, piece_position):
        for square in self.board_squares:
            if square.pos == piece_position:
                return square

    def handle_click_on_board(self, mouse_x, mouse_y):
        x = int(mouse_x / self.square_width) + 1
        y = int((self.width - mouse_y) / self.square_width) + 1
        pos = (x, y)
        if self.selected_piece_position == (0, 0):
            if self.get_square(pos).piece_notation != 'e':
                self.selected_piece_position = pos
                self.set_legal_moves()
            self.draw_board()
        else:
            self.selected_square_position = pos
            if self.legal_moves_of_selected_piece.count(pos) == 1:
                self.move_piece()

            self.selected_square_position = (0, 0)
            self.selected_piece_position = (0, 0)
            self.legal_moves_of_selected_piece = []
            self.draw_board()

    def set_legal_moves(self):
        pos = self.selected_piece_position
        if self.get_square(pos).piece_notation[1] == 'p':
            pawn = Pawn(pos, self)
            self.legal_moves_of_selected_piece = pawn.evaluate_legal_moves()
        elif self.get_square(pos).piece_notation[1] == 'r':
            rook = Rook(pos, self)
            self.legal_moves_of_selected_piece = rook.evaluate_legal_moves()
        elif self.get_square(pos).piece_notation[1] == 'k':
            king = King(pos, self)
            self.legal_moves_of_selected_piece = king.evaluate_legal_moves()

    def move_piece(self):
        piece_notation = self.get_square(self.selected_piece_position).piece_notation
        self.get_square(self.selected_piece_position).piece_notation = 'e'
        self.get_square(self.selected_square_position).piece_notation = piece_notation

    def draw_board(self):
        for y in range(1, 9):
            for x in range(1, 9):
                pos = (x, y)
                if (x + y) % 2 == 1:
                    color = COLOR_ODD
                else:
                    color = COLOR_EVEN

                square_start_point_x = (x - 1) * self.square_width
                square_start_point_y = self.width - (y * self.square_width)
                square_rect = pygame.draw.rect(self.screen, color, (
                    square_start_point_x, square_start_point_y, self.square_width, self.square_width))

                if self.get_square(pos).piece_notation != "e":
                    image = get_piece_image(self.get_square(pos).piece_notation)
                    image = pygame.transform.scale(image, (self.square_width - 10, self.square_width - 10))
                    image_rect = image.get_rect()
                    image_rect.center = square_rect.center
                    self.screen.blit(image, image_rect)
                self.get_square(pos)
                if self.legal_moves_of_selected_piece.count(pos) == 1:
                    pygame.draw.circle(self.screen, "red", square_rect.center, 20)

                pygame.display.flip()
