import pygame, sys
from pygame.locals import *
from board import *

WINDOW = None
W_COLOR = (255, 255, 255)
B_COLOR = (0, 0, 0)
BG_COLOR = (76, 175, 80)
def draw_board(r):
    for i in range(8):
        for j in range(8):
            pygame.draw.rect(WINDOW, BG_COLOR, (j * 80 + 2, i * 80 + 2, 76, 76))
            if r.b[i][j] == WHITE:
                pygame.draw.circle(WINDOW, W_COLOR, (j * 80 + 40, i * 80 + 40), 30)
            elif r.b[i][j] == BLACK:
                pygame.draw.circle(WINDOW, B_COLOR, (j * 80 + 40, i * 80 + 40), 30)
def main():
    reversi = board()
    pygame.init()
    global WINDOW
    WINDOW = pygame.display.set_mode((640, 640))
    pygame.display.set_caption('Reversi Game')
    WINDOW.fill(B_COLOR)
    fps = pygame.time.Clock()
    draw_board(reversi)
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                row = mousey // 80
                col = mousex // 80
                if reversi.is_legal_move((row, col)):
                    reversi.make_move(row, col)
                    reversi.change_turn()
                    reversi.calc_legal_moves()
                
        draw_board(reversi)
        pygame.display.update()
        fps.tick(30)
if __name__ == '__main__':
    main()
