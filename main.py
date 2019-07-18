'''
SimplePaint - Programa para pequenos desenhos
Intuito exclusivamente academico. PyGame
'''

# -*- coding: utf-8 -*-
from typing import List, Any
import pygame, os
from pygame.locals import *


def buttons():
    #  Create Buttons
    posButtons.append(setPosButtonsX[0])
    i = 0
    for cor in colors:
        pygame.draw.rect(screen, colors[cor], (posButtons[i], setPosButtonsY, sizeofButtons[0], sizeofButtons[1]))
        posButtons.append(posButtons[i] + sizeofButtons[0] + setPosButtonsX[1])
        i += 1


def set_menus():
    # Place Menu
    pygame.draw.rect(screen, menu_color, (posMenus['Header'][0], posMenus['Header'][1], sizeMenu[0], sizeMenu[1]))
    pygame.draw.rect(screen, menu_color, (posMenus['Footer'][0], posMenus['Footer'][1], sizeMenu[0], sizeMenu[1]))
    buttons()


def display_screen():
    # Screen Elements
    screen.fill((255, 255, 255))
    set_menus()
    pygame.draw.rect(screen, cor, (572, 5, 25, 25))  # Mostrar a cor atual
    screen.blit(titulo, (250, 20))
    screen.blit(clean, (10, 15))
    screen.blit(pScreen, (10, 30))


def screenshot():
    numberShot = 0
    salve = False
    while not salve:
        nomeArquivo = 'img{0}.jpg'.format(numberShot)
        sub = screen.subsurface(0, sizeMenu[1], 600, 600 - 2*sizeMenu[1])
        if os.listdir('_ScreenShots') == []:
            pygame.image.save(sub, "_ScreenShots/{0}".format(nomeArquivo))
        else:
            for x in os.listdir('_ScreenShots'):
                if nomeArquivo == x:
                    numberShot += 1
                    salve = False
                    break
                salve = True
            if salve:
                pygame.image.save(sub, "_ScreenShots/{0}".format(nomeArquivo))




# set screen and clock
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))
pygame.display.set_caption("Simple Paint")
clock = pygame.time.Clock()

# variables
#   Colors
colors = {'blue': (0, 0, 255), 'green': (0, 255, 0), 'red': (255, 0, 0), 'yellow': (255, 255, 0), 'white':
    (255, 255, 255), 'black': (0, 0, 0)}

cor = colors['black']  # Initial Colors
menu_color = (50, 50, 50)

#   Buttons
sizeofButtons = [75, 50]  # [0]Width, [1] Height
posButtons = []
setPosButtonsX = [20, 20]  # [0]Initial Pos, [1] Spacing
setPosButtonsY = 540

#   Menu
posMenus = {'Header': (0, 0), 'Footer': (0, 520)}
sizeMenu = (600, 80)  # [0] Width, [1] height
offSetMouseTouch = 5


# Fonts
pygame.font.init()
styleTitle = pygame.font.SysFont("Arial", 25)
styleShots = pygame.font.SysFont("Arial", 15)
#   Titulo
titulo = styleTitle.render("Simple Paint", 1, colors['white'])
#   Instruções
clean = styleShots.render("Press 'r' to clean screen", 1, colors['white'])
pScreen = styleShots.render("Press 's' to print screen", 1, colors['white'])
# Init
display_screen()

# Loop
while True:
    # ShotCuts
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_r:
                display_screen()
            if event.key == K_s:
                screenshot()

    # Controllers
    mouse_pos = pygame.mouse.get_pos()
    # interactions
    if pygame.mouse.get_pressed()[0]:
        # Button Colors
        if (posButtons[0] < mouse_pos[0] < (posButtons[0]+sizeofButtons[0])) and (540 < mouse_pos[1] < 590):
            cor = colors['blue']
        elif (posButtons[1] < mouse_pos[0] < (posButtons[1]+sizeofButtons[0])) and (540 < mouse_pos[1] < 590):
            cor = colors['green']
        elif (posButtons[2] < mouse_pos[0] < (posButtons[2]+sizeofButtons[0])) and (540 < mouse_pos[1] < 590):
            cor = colors['red']
        elif (posButtons[3] < mouse_pos[0] < (posButtons[3]+sizeofButtons[0])) and (540 < mouse_pos[1] < 590):
            cor = colors['yellow']
        elif (posButtons[4] < mouse_pos[0] < (posButtons[4]+sizeofButtons[0])) and (540 < mouse_pos[1] < 590):
            cor = colors['white']
        elif (posButtons[5] < mouse_pos[0] < (posButtons[5]+sizeofButtons[0])) and (540 < mouse_pos[1] < 590):
            cor = colors['black']


        pygame.draw.rect(screen, cor, (572, 5, 25, 25))  # Current Color
        # Drawing 
        if pygame.mouse.get_pressed()[0] and (not(mouse_pos[1] >= posMenus['Footer'][1] - offSetMouseTouch)
                                              and not(mouse_pos[1] <= posMenus['Header'][1]+sizeMenu[1] + offSetMouseTouch)):
            pygame.draw.circle(screen, cor, mouse_pos, 5)

    # Late
    pygame.display.update()
