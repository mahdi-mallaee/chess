import pygame
from classes.board import Board

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BOARD_WIDTH = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
isBoardDrawn = False
board = Board(BOARD_WIDTH, screen)

while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Board.handle_click_on_board(board, mouse_x, mouse_y)

    if not isBoardDrawn:
        Board.initial_board(board)
        isBoardDrawn = True
