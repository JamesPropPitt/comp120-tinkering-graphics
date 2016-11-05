import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()
pygame.font.init()

# set up window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 875

# set up colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Load Images
bequietImg = pygame.image.load("shh.png")
bequietImg = pygame.transform.scale(bequietImg,(1280, 875))
classicImg = pygame.image.load("classic.jpg")
classicImg = pygame.transform.scale(classicImg,(1280, 875))
kitchencatsImg = pygame.image.load('kitchencats.jpg')
loneknightImg = pygame.image.load("loneknight.png")
loneknightImg = pygame.transform.scale(loneknightImg,(1280, 875))
knightIcon = pygame.image.load('shh.png')

#Set up fonts
memefont = pygame.font.SysFont('Impact', 72)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.fill(WHITE)
pygame.display.set_caption('Memes')
clock = pygame.time.Clock()

"""Ed's Lecture Meme (Press 'e' on keyboard)"""
def edlecture():

    # Set edlecture meme text
    Fontimg = memefont.render("When Ed's lecture is", 1, WHITE)
    Fontimg2 = memefont.render("9AM monday morning", 1, WHITE)
    # Blit edlecture meme to screen
    window.fill(WHITE)
    window.blit(classicImg, (0, 0))
    window.blit(Fontimg, (25, 0))
    window.blit(Fontimg2, (450, 740))

"""Crusading Meme (Press 'c' on keyboard)"""
def crusadememe():

    # Add icon and caption
    knightIcon = pygame.image.load('knight.png')
    pygame.display.set_icon(knightIcon)
    pygame.display.set_caption("Take back Jerusalem")

    # Set crusade meme text
    Fontimg = memefont.render("When you were supposed to go crusading", 1, WHITE)
    Fontimg2 = memefont.render("but your squad ditches you", 1, WHITE)

    # Blit crusadememe to screen
    window.fill(WHITE)
    window.blit(loneknightImg, (0, 0))
    window.blit(Fontimg, (20, 10))
    window.blit(Fontimg2, (120, 450))

"""Homework Meme (Press 'h' on keyboard)"""
def homeworkmeme():

    pygame.display.set_icon(knightIcon)
    pygame.display.set_caption("pls stop")

    # Meme text font, size, anti-aliasing and colour
    Fontimg = memefont.render("When someone is about to remind", 1, WHITE)
    Fontimg2 = memefont.render("the teacher about homework", 1, WHITE)

    # Loads, draws and updates the meme/display
    window.fill(WHITE)
    window.blit(bequietImg, (0, 0))
    window.blit(Fontimg, (11, 10))
    window.blit(Fontimg2, (32, 415))

"""Kitchen Cat Meme (Press 'k' on keyboard)"""
def kitchencats():
    text = memefont.render('When a flatmate', True, WHITE)
    text2 = memefont.render("won't wash up.", True, WHITE)
    window.fill(WHITE)
    window.blit(kitchencatsImg, (0, 0))
    window.blit(text, (20, 10))
    window.blit(text2, (60, 100))

"""Make image Red (Press 'r' on keyboard)"""
def makered():
    for Y in range(0, WINDOW_HEIGHT):
        for X in range(0, WINDOW_WIDTH):

            RED = window.get_at((X, Y)).r
            GREEN = window.get_at((X, Y)).g
            BLUE = window.get_at((X, Y)).b

            RED = 255
            GREEN = 255 - GREEN
            BLUE = 255 - BLUE

            PXArray[X, Y] = (RED, GREEN, BLUE)

"""Make image Green (Press 'g' on keyboard)"""
def makegreen():
    for Y in range(0, WINDOW_HEIGHT):
        for X in range(0, WINDOW_WIDTH):
            RED = window.get_at((X, Y)).r
            GREEN = window.get_at((X, Y)).g
            BLUE = window.get_at((X, Y)).b

            RED = 255 - RED
            GREEN = 255
            BLUE = 255 - BLUE

            PXArray[X, Y] = (RED, GREEN, BLUE)

"""Make image Blue (Press 'b' on keyboard)"""
def makeblue():
    for Y in range(0, WINDOW_HEIGHT):
        for X in range(0, WINDOW_WIDTH):
            RED = window.get_at((X, Y)).r
            GREEN = window.get_at((X, Y)).g
            BLUE = window.get_at((X, Y)).b

            RED = 255 - Red
            GREEN = 255 - GREEN
            BLUE = 255

            PXArray[X, Y] = (RED, GREEN, BLUE)

"""Convert image to negative (Press 'n' on keyboard)"""
def negative():
    for Y in range(0, WINDOW_HEIGHT):
        for X in range(0, WINDOW_WIDTH):
            RED = window.get_at((X, Y)).r
            GREEN = window.get_at((X, Y)).g
            BLUE = window.get_at((X, Y)).b

            RED = 255 - RED
            GREEN = 255 - GREEN
            BLUE = 255 - BLUE

            PXArray[X, Y] = (RED, GREEN, BLUE)

# set up program loop
while True:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_k:
            kitchencats()
        if event.type == KEYDOWN and event.key == K_r:
            PXArray = pygame.PixelArray(window)
            makered()
            del PXArray
        if event.type == KEYDOWN and event.key == K_g:
            PXArray = pygame.PixelArray(window)
            makegreen()
            del PXArray
        if event.type == KEYDOWN and event.key == K_b:
            PXArray = pygame.PixelArray(window)
            makeblue()
            del PXArray
        if event.type == KEYDOWN and event.key == K_n:
            PXArray = pygame.PixelArray(window)
            negative()
            del PXArray
        if event.type == KEYDOWN and event.key == K_e:
            edlecture()
        if event.type == KEYDOWN and event.key == K_c:
            crusadememe()
        if event.type == KEYDOWN and event.key == K_h:
            homeworkmeme()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if pressed[K_ESCAPE]:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(200)

pygame.quit()
quit()