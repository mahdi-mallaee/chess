import pygame
from classes.square import Square

COLOR_ODD = (100, 100, 100)
COLOR_EVEN = (200, 200, 200)
NONE_POS = (0, 0)


class Board:
    def __init__(self, width, screen):
        self.screen = screen
        self.width = width
        self.square_width = width / 8
        self.initial_board_string = "wr-wn-wb-wq-wk-wb-wn-wr/wp-wp-wp-wp-wp-wp-wp-wp/8/8/8/8/" \
                                    "bp-bp-bp-bp-bp-bp-bp-bp/br-bn-bb-bq-bk-bb-bn-br"
        self.board_squares = self.translate_board_string(self.initial_board_string)
        self.selected_square_position = NONE_POS
        self.selected_piece_position = NONE_POS
        self.selected_piece_legal_moves = []

    def initial_board(self):
        self.board_squares = self.translate_board_string(self.initial_board_string)
        self.draw_board()

    def translate_board_string(self, board_string):
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
                        square = Square(self, (x, y), 'e')
                        board.append(square)
                else:
                    x += 1
                    square = Square(self, (x, y), notation)
                    board.append(square)
        return board

    def get_square(self, piece_position):
        for square in self.board_squares:
            if square.pos == piece_position:
                return square

    def handle_board_click(self, mouse_x, mouse_y):
        x = int(mouse_x / self.square_width) + 1
        y = int((self.width - mouse_y) / self.square_width) + 1
        pos = (x, y)
        piece_notation = self.get_square(pos).piece_notation
        if self.selected_piece_position == NONE_POS:
            if piece_notation != 'e':
                self.selected_piece_position = pos
                self.set_legal_moves()
            self.draw_board()
        else:
            self.selected_square_position = pos
            if self.selected_piece_legal_moves.count(pos) == 1:
                self.move_piece()

            self.clear_selected_piece()
            self.draw_board()

    def clear_selected_piece(self):
        self.selected_square_position = NONE_POS
        self.selected_piece_position = NONE_POS
        self.selected_piece_legal_moves = []

    def set_legal_moves(self):
        pos = self.selected_piece_position
        self.selected_piece_legal_moves = self.get_square(pos).get_legal_moves()

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

                square = self.get_square(pos)
                if square.piece_notation != "e":
                    image = square.get_piece_image()
                    image = pygame.transform.scale(image, (self.square_width - 10, self.square_width - 10))
                    image_rect = image.get_rect()
                    image_rect.center = square_rect.center
                    self.screen.blit(image, image_rect)

                if self.selected_piece_legal_moves.count(pos) == 1:
                    pygame.draw.circle(self.screen, "red", square_rect.center, 20)

                pygame.display.flip()
