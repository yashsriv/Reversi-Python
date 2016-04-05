#!/usr/bin/env python3
import pygame, sys
from pygame.locals import *
from board import *

WINDOW = None
W_COLOR = (255, 255, 255)
B_COLOR = (0, 0, 0)
BG_COLOR = (76, 175, 80)
status = ''
def draw_board(r):
    for i in range(8):
        for j in range(8):
            pygame.draw.rect(WINDOW, BG_COLOR, (j * 80 + 1, i * 80 + 1, 78, 78))
            if r.b[i][j] == WHITE:
                pygame.draw.circle(WINDOW, W_COLOR, (j * 80 + 40, i * 80 + 40), 30)
            elif r.b[i][j] == BLACK:
                pygame.draw.circle(WINDOW, B_COLOR, (j * 80 + 40, i * 80 + 40), 30)

def draw_whose_turn(r):
    fontObj = pygame.font.SysFont('linuxlibertinedisplayo', 18)
    if r.turn == BLACK:
        turn = "Black's Turn"
    else:
        turn = "White's Turn"
    textSurfaceObj = fontObj.render(turn, True, B_COLOR, BG_COLOR)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (160, 660)
    WINDOW.blit(textSurfaceObj, textRectObj)

def draw_status():
    fontObj = pygame.font.SysFont('linuxlibertinedisplayo', 18)
    textSurfaceObj = fontObj.render(status, True, B_COLOR, BG_COLOR)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (480, 660)
    WINDOW.blit(textSurfaceObj, textRectObj)

def draw_count(r):
    white = sum(l.count(WHITE) for l in r.b)
    black = sum(l.count(BLACK) for l in r.b)
    font_obj = pygame.font.SysFont('linuxlibertinedisplayo', 18)
    text_surface_obj = font_obj.render('WHITE', True, B_COLOR, W_COLOR)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (700, 60)
    text_surface_obj_2 = font_obj.render(str(white), True, B_COLOR, W_COLOR)
    text_rect_obj_2 = text_surface_obj_2.get_rect()
    text_rect_obj_2.center = (700, 80)
    pygame.draw.rect(WINDOW, W_COLOR, ( 640 + 1, text_rect_obj.top, 98, text_rect_obj_2.bottom - text_rect_obj.top))
    WINDOW.blit(text_surface_obj, text_rect_obj)
    WINDOW.blit(text_surface_obj_2, text_rect_obj_2)

    text_surface_obj = font_obj.render('BLACK', True, W_COLOR, B_COLOR)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (700, 120)
    text_surface_obj_2 = font_obj.render(str(black), True, W_COLOR, B_COLOR)
    text_rect_obj_2 = text_surface_obj_2.get_rect()
    text_rect_obj_2.center = (700, 140)
    pygame.draw.rect(WINDOW, B_COLOR, ( 640 + 1, text_rect_obj.top, 98, text_rect_obj_2.bottom - text_rect_obj.top))
    WINDOW.blit(text_surface_obj, text_rect_obj)
    WINDOW.blit(text_surface_obj_2, text_rect_obj_2)

def main():
    reversi = board()
    pygame.init()
    global WINDOW
    WINDOW = pygame.display.set_mode((740, 680))
    pygame.display.set_caption('Reversi Game')
    WINDOW.fill(B_COLOR)
    fps = pygame.time.Clock()
    draw_board(reversi)
    pygame.draw.rect(WINDOW, BG_COLOR, ( 1, 640 + 1, 638, 38))
    pygame.draw.rect(WINDOW, BG_COLOR, ( 640 + 1, 1, 98, 678))
    pygame.display.update()
    global status
    status = 'Please Play your move'

    while not reversi.is_game_over():
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
                    status = 'Please Play your move'
                else:
                    status = 'Invalid Move'
        pygame.draw.rect(WINDOW, BG_COLOR, ( 1, 640 + 1, 638, 38))
        pygame.draw.rect(WINDOW, BG_COLOR, ( 640 + 1, 1, 98, 678))
        draw_whose_turn(reversi)
        draw_status()
        draw_count(reversi)
        draw_board(reversi)
        pygame.display.update()
        fps.tick(30)
    if reversi.winner == BLACK:
        status = 'Black Wins'
        pic = pygame.image.load('../res/black_win.png')
    else :
        status = 'White Wins'
        pic = pygame.image.load('../res/white_win.png')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(WINDOW, BG_COLOR, ( 1, 640 + 1, 638, 38))
        draw_status()
        draw_board(reversi)
        alpha = WINDOW.convert_alpha()
        alpha.blit(pic,(0,0))
        WINDOW.blit(alpha,(0,0))
        pygame.display.update()
        fps.tick(30)
if __name__ == '__main__':
    main()
