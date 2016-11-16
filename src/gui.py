#!/usr/bin/env python3
"""
GUI for Reversi Game Board as well as event handling
"""
import pygame, sys
from pygame.locals import *
from board import *

WINDOW = None
W_COLOR = (255, 255, 255)
B_COLOR = (0, 0, 0)
BG_COLOR = (42, 83, 65)
STATUS = ''
TWO_PLAYER = False

class Button():
    """
    A class representing a button
    """
    def __init__(self, rectangular_area, on_focus_color, normal_color, text):
        """
        Give default values as per parameters passed
        """
        self.rectang = rectangular_area
        self.on_focus = on_focus_color
        self.normal = normal_color
        self.text = text
    def draw(self, focus):
        """
        Draw depending upon whether it is in focus or not
        """
        if focus:
            pygame.draw.rect(WINDOW, self.on_focus, self.rectang)
        else:
            pygame.draw.rect(WINDOW, self.normal, self.rectang)
        fontObj = pygame.font.SysFont('linuxlibertinedisplayo', 28)
        textSurfaceObj = fontObj.render(self.text, True, (0, 0, 0))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = self.rectang.center
        WINDOW.blit(textSurfaceObj, textRectObj)

def draw_buttons(buttons, mousex, mousey):
    """
    Call the draw function of all buttons
    """
    for button in buttons:
        if button.rectang.collidepoint(mousex, mousey):
            button.draw(True)
        else:
            button.draw(False)

def show_gui():
    """
    Draw initial gui
    """
    done = False
    buttons = []
    buttons.append(Button(pygame.Rect(100, 320, 120, 40), (46, 125, 50), BG_COLOR, '1 Player'))
    buttons.append(Button(pygame.Rect(300, 320, 120, 40), (46, 125, 50), BG_COLOR, '2 Player'))
    buttons.append(Button(pygame.Rect(500, 320, 80, 40), (46, 125, 50), BG_COLOR, 'Exit'))
    WINDOW.fill(BG_COLOR)
    logo = pygame.image.load('../res/logo.png')
    aca = pygame.image.load('../res/aca.png')
    WINDOW.blit(logo, (90, 40))
    WINDOW.blit(aca, (0, 460))
    mousex, mousey = (0, 0)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.locals.MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == pygame.locals.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.rectang.collidepoint(event.pos):
                        if button.text == '1 Player':
                            done = True
                        elif button.text == '2 Player':
                            global TWO_PLAYER
                            TWO_PLAYER = True
                            done = True
                        else:
                            pygame.quit()
                            sys.exit()
        draw_buttons(buttons, mousex, mousey)
        pygame.display.update()

def main():
    """
    The main function
    """
    global WINDOW
    pygame.init()
    WINDOW = pygame.display.set_mode((640, 640))
    pygame.display.set_caption('Reversi Game')
    show_gui()
    start_game()


def draw_board(r):
    """
    Draw the board
    """
    for i in range(8):
        for j in range(8):
            pygame.draw.rect(WINDOW, BG_COLOR, (j * 80 + 1, i * 80 + 1, 78, 78))
            if r.b[i][j] == WHITE:
                pygame.draw.circle(WINDOW, W_COLOR, (j * 80 + 40, i * 80 + 40), 30)
            elif r.b[i][j] == BLACK:
                pygame.draw.circle(WINDOW, B_COLOR, (j * 80 + 40, i * 80 + 40), 30)
    for (x, y) in r.legal_moves:
        pygame.draw.circle(WINDOW, (0, 150, 136), (y * 80 + 40, x * 80 + 40), 30)


def draw_whose_turn(r):
    """
    Show whose turn it is at the bottom
    """
    fontObj = pygame.font.SysFont('linuxlibertinedisplayo', 18)
    if r.turn == BLACK:
        turn = "Black's Turn"
        textSurfaceObj = fontObj.render(turn, True, W_COLOR, B_COLOR)
    else:
        turn = "White's Turn"
        textSurfaceObj = fontObj.render(turn, True, B_COLOR, W_COLOR)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (160, 660)
    if r.turn == BLACK:
        pygame.draw.rect(WINDOW, B_COLOR, (textRectObj.left, 640 + 1, textRectObj.right - textRectObj.left, 38))
    else:
        pygame.draw.rect(WINDOW, W_COLOR, (textRectObj.left, 640 + 1, textRectObj.right - textRectObj.left, 38))
    WINDOW.blit(textSurfaceObj, textRectObj)

def draw_status():
    """
    Show STATUS messages such as who won
    """
    fontObj = pygame.font.SysFont('linuxlibertinedisplayo', 18)
    textSurfaceObj = fontObj.render(STATUS, True, B_COLOR, (46, 125, 60))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (480, 660)
    pygame.draw.rect(WINDOW, (46, 125, 60), (textRectObj.left, 640 + 1, textRectObj.right - textRectObj.left, 38))
    WINDOW.blit(textSurfaceObj, textRectObj)

def draw_count(r):
    """
    Show count of each player's tokens
    """
    white = sum(l.count(WHITE) for l in r.b)
    black = sum(l.count(BLACK) for l in r.b)
    font_obj = pygame.font.SysFont('linuxlibertinedisplayo', 18)
    text_surface_obj = font_obj.render('WHITE', True, B_COLOR, W_COLOR)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (700, 60)
    text_surface_obj_2 = font_obj.render(str(white), True, B_COLOR, W_COLOR)
    text_rect_obj_2 = text_surface_obj_2.get_rect()
    text_rect_obj_2.center = (700, 80)
    pygame.draw.rect(WINDOW, W_COLOR, (640 + 1, text_rect_obj.top, 98, text_rect_obj_2.bottom - text_rect_obj.top))
    WINDOW.blit(text_surface_obj, text_rect_obj)
    WINDOW.blit(text_surface_obj_2, text_rect_obj_2)

    text_surface_obj = font_obj.render('BLACK', True, W_COLOR, B_COLOR)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (700, 120)
    text_surface_obj_2 = font_obj.render(str(black), True, W_COLOR, B_COLOR)
    text_rect_obj_2 = text_surface_obj_2.get_rect()
    text_rect_obj_2.center = (700, 140)
    pygame.draw.rect(WINDOW, B_COLOR, (640 + 1, text_rect_obj.top, 98, text_rect_obj_2.bottom - text_rect_obj.top))
    WINDOW.blit(text_surface_obj, text_rect_obj)
    WINDOW.blit(text_surface_obj_2, text_rect_obj_2)

def start_game():
    """
    Start actual game loop
    """
    reversi = board()
    global WINDOW
    WINDOW = pygame.display.set_mode((740, 680))
    pygame.display.set_caption('Reversi Game')
    WINDOW.fill(B_COLOR)
    fps = pygame.time.Clock()
    draw_board(reversi)
    pygame.draw.rect(WINDOW, BG_COLOR, (1, 640 + 1, 638, 38))
    pygame.draw.rect(WINDOW, BG_COLOR, (640 + 1, 1, 98, 678))
    pygame.display.update()
    global STATUS
    STATUS = 'Please Play your move'
    buttons = []
    buttons.append(Button(pygame.Rect(640, 640, 100, 40), (46, 125, 50), BG_COLOR, 'Exit'))
    mousex, mousey = (0, 0)
    while not reversi.is_game_over():
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                for button in buttons:
                    if button.rectang.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                mousex, mousey = event.pos
                row = mousey // 80
                col = mousex // 80
                if reversi.is_legal_move((row, col)):
                    reversi.make_move(row, col)
                    reversi.change_turn()
                    reversi.calc_legal_moves()
                    if not TWO_PLAYER and not reversi.is_game_over():
                        STATUS = 'I am thinking'
                        draw_status()
                        draw_count(reversi)
                        draw_board(reversi)
                        pygame.display.update()
                        reversi.computer_move()
                        reversi.change_turn()
                        reversi.calc_legal_moves()
                    STATUS = 'Please Play your move'
                else:
                    STATUS = 'Invalid Move'
        pygame.draw.rect(WINDOW, BG_COLOR, (1, 640 + 1, 638, 38))
        pygame.draw.rect(WINDOW, BG_COLOR, (640 + 1, 1, 98, 678))
        draw_whose_turn(reversi)
        draw_status()
        draw_count(reversi)
        draw_board(reversi)
        draw_buttons(buttons, mousex, mousey)
        pygame.display.update()
        fps.tick(30)
    if reversi.winner == BLACK:
        STATUS = 'Black Wins'
        pic = pygame.image.load('../res/black_win.png')
    else:
        STATUS = 'White Wins'
        pic = pygame.image.load('../res/white_win.png')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                for button in buttons:
                    if button.rectang.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
        pygame.draw.rect(WINDOW, BG_COLOR, (1, 640 + 1, 638, 38))
        draw_status()
        draw_board(reversi)
        alpha = WINDOW.convert_alpha()
        alpha.blit(pic, (0, 0))
        WINDOW.blit(alpha, (0, 0))
        draw_buttons(buttons, mousex, mousey)
        pygame.display.update()
        fps.tick(30)
if __name__ == '__main__':
    main()
