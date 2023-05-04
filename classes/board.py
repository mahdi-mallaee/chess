import pygame
from classes.square import Square
from classes.eboard import EBoard

COLOR_ODD = (100, 100, 100)
COLOR_EVEN = (200, 200, 200)
NONE_POS = (0, 0)
LEGAL_MOVE_COLOR = 'red'
SQUARE_PADDING = 15


class Board:
    def __init__(self, width, screen):
        self.screen = screen
        self.width = width
        self.square_width = width / 8
        self.initial_board_string = 'RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr w KQkq - 0 1'
        self.board_string = self.initial_board_string
        self.board_squares = self.translate_fen(self.initial_board_string)
        self.selected_square_position = NONE_POS
        self.selected_piece_position = NONE_POS
        self.selected_piece_legal_moves = []
        self.turn_color = 'w'

    def initial_board(self):
        self.board_squares = self.translate_fen(self.initial_board_string)
        self.draw_board()

    def change_turn(self):
        if self.turn_color == 'w':
            self.turn_color = 'b'
        else:
            self.turn_color = 'w'

    def translate_fen(self, board_string):
        board_string = str(board_string)

        rows = board_string.split("/")
        additional_info = rows[-1].split(' ')
        rows.remove(rows[-1])
        rows.append(additional_info[0])
        additional_info.remove(additional_info[0])

        turn_color = additional_info[0]
        self.turn_color = turn_color

        board = []
        y = 0
        for row in rows:
            y += 1
            x = 0
            for notation in row:
                if notation.isnumeric():
                    empty_squares_count = int(notation)
                    for i in range(0, empty_squares_count):
                        x += 1
                        square = Square(self, (x, y), 'e', 'e')
                        board.append(square)
                else:
                    color = 'w' if notation.isupper() else 'b'
                    x += 1
                    square = Square(self, (x, y), notation.lower(), color)
                    board.append(square)

        return board

    def get_square(self, piece_position):
        for square in self.board_squares:
            if square.pos == piece_position:
                return square

    def get_squares_by_notation(self, notation, color):
        squares = []
        for s in self.board_squares:
            if s.notation == notation and s.color == color:
                squares.append(s)
        return squares

    def handle_board_click(self, mouse_x, mouse_y):
        x = int(mouse_x / self.square_width) + 1
        y = int((self.width - mouse_y) / self.square_width) + 1
        pos = (x, y)
        square = self.get_square(pos)

        if self.selected_piece_position != NONE_POS and self.selected_piece_legal_moves.count(pos) == 1:
            self.selected_square_position = pos
            self.change_turn()
            self.move_piece()
            self.clear_selected_piece()
            self.draw_board()
        else:
            if not square.is_empty() and square.color == self.turn_color:
                self.selected_piece_position = pos
                self.set_legal_moves()
                self.draw_board()
            else:
                self.clear_selected_piece()
                self.draw_board()

    def is_in_check(self):
        square = self.get_squares_by_notation('k', self.turn_color)[0]
        is_in_check = square.is_in_check()
        return is_in_check

    def checkmate_check(self):
        if self.is_in_check():
            moves = []
            for s in self.board_squares:
                if not s.is_empty() and s.color == self.turn_color:
                    legal_moves = self.get_square(s.pos).get_legal_moves()
                    for move in legal_moves:
                        e_board = EBoard(self.board_squares, self.turn_color)
                        e_board.move_piece(s.pos, move)
                        if not e_board.is_in_check():
                            moves.append(move)
            if len(moves) > 0:
                return False
            else:
                return True
        else:
            return False

    def clear_selected_piece(self):
        self.selected_square_position = NONE_POS
        self.selected_piece_position = NONE_POS
        self.selected_piece_legal_moves = []

    def set_legal_moves(self):
        pos = self.selected_piece_position
        moves = []
        legal_moves = self.get_square(pos).get_legal_moves()
        for move in legal_moves:
            e_board = EBoard(self.board_squares, self.turn_color)
            e_board.move_piece(pos, move)
            if not e_board.is_in_check():
                moves.append(move)
        self.selected_piece_legal_moves = moves

    def move_piece(self):
        piece = self.get_square(self.selected_piece_position)
        square = self.get_square(self.selected_square_position)
        square.notation = piece.notation
        square.color = piece.color
        piece.notation = 'e'
        piece.color = 'e'
        if self.checkmate_check():
            print(self.turn_color + ' is loser')

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
                if not square.is_empty():
                    image = square.get_piece_image()
                    image = pygame.transform.scale(image, (
                        self.square_width - SQUARE_PADDING, self.square_width - SQUARE_PADDING))
                    image_rect = image.get_rect()
                    image_rect.center = square_rect.center
                    self.screen.blit(image, image_rect)

                if self.selected_piece_legal_moves.count(pos) == 1:
                    pygame.draw.circle(self.screen, LEGAL_MOVE_COLOR, square_rect.center, 15)

                pygame.display.flip()
