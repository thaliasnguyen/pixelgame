import pygame
import os
import sys
import time
from pygame.locals import *

##########  COLORS ############################
white = (255,255,255)
black = (0,0,0)

red = (200,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (34,177,76)
light_green = (0,255,0)

######### Title and icon ###########################
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('bleh') ## title
icon = pygame.image.load('nickright.png') ### icon
pygame.display.set_icon(icon)

##########  images sources  #############
bg1 = pygame.image.load("bg1.jpg")
bg2 = pygame.image.load("bg2.jpg")
playerimg = pygame.image.load('MC1.png')
clock = pygame.time.Clock()
currentScreen = bg1
global gameOver #### global gameOver
global player  ##for the mc
global running ## tu run the game
global Start_x ## current position of mc
global Start_y ## current position of mc
global current_x
global current_y
####### to continue the game  ###############
def gameLoop():
    global gameOver
    gameExit = False
    gameOver = False


################ M A I N   C H A R A C T E R   ##################
class Player(object):
    def __init__(self):
        # define player
        self.image = pygame.image.load("MC1.png")
        self.x = 100
        self.y = 100
        global Start_x
        global Start_y
        Start_x = self.x
        Start_y = self.y

    def handle_keys(self):
        # player movement
        key = pygame.key.get_pressed()
        dist = 10
        if key[pygame.K_DOWN]:
            #current_y = current_y + dist
            global Start_y
            global current_y
            current_y = Start_y + dist

        elif key[pygame.K_UP]:
            global Start_y
            Start_y -=dist

        if key[pygame.K_RIGHT]:
            global Start_x
            Start_x += dist

        elif key[pygame.K_LEFT]:
            global Start_x
            Start_x -= dist

    # def update(self):
    #     # player moving through different scenes
    #     global currentScreen
    #     if player.y >= 600:
    #         if currentScreen == bg1: ## bg 1 vs bg 2
    #             player.y = 0
    #             gameDisplay.fill((0,0,0))
    #             gameDisplay.blit(bg2,(0,0))
    #             currentScreen = bg2
    #
    #         elif currentScreen == bg2: ## bg 2 in place
    #             gameDisplay.fill((0,0,0))
    #             gameDisplay.blit(bg2,(0,0))
    #             currentScreen = bg2
    #             player.y = 600
    #
    #     elif player.y <= 0:
    #         if currentScreen == bg2: ## bg2 vs bg1
    #             player.y = 600
    #             gameDisplay.fill((0,0,0))
    #             gameDisplay.blit(bg1,(0,0))
    #             currentScreen = bg1
    #
    #         elif currentScreen == bg1: ## bg1 in place
    #             gameDisplay.fill((0,0,0))
    #             gameDisplay.blit(bg1,(0,0))
    #             currentScreen = bg1
    #             player.y = 0
     ###### The sprite is going from top to bottom :D

    def draw(self, surface):
        # to move the cat freely :D
        """ Draw on surface"""
        surface.blit(self.image, (Start_x, Start_y))


################## M E S S A G E S #####################################

######## py.game.font.Font - custom font downloaded  #####
pygame.font.init()
all_fonts = pygame.font.get_fonts()
smallfont = pygame.font.SysFont("comicsansms", 25)
mediumfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 100)

##########   define the message/ dialogs to the AI ###############
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

############ to make the dialogs pretty (if needed) ################
def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, red)
    elif size == "medium":
        textSurface = medfont.render(text, True, green)
    elif size == "large":
        textSurface = largefont.render(text, True, black)
    return textSurface, textSurface.get_rect()

################ #####################
def game_running ():
    global running
    running = True
    while running :
    ############  when you are not in game over #########
        global gameOver
        gameOver = False
        while gameOver != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
            currentScreen = bg1
            pygame.image.load("bg1.jpg")
            global player
            player = Player()
            player.handle_keys()
            player.draw(currentScreen)
            #player.update()
            gameDisplay.fill((0,0,0))
            gameDisplay.blit(currentScreen, (100,100))
            pygame.display.update()
            clock.tick(40)


    gameLoop()

################### I N T R O   S C R E E N  #################################
def gameIntro ():
    intro = True
    ########### layout of the intro screen #####################
    gameDisplay.fill(white)
    message_to_screen("Welcome to ___", green, -100, size = "large")
    message_to_screen("...", black, -30, size = "small")
    message_to_screen("...", black, 10, size = "small")
    message_to_screen("...", black, 50, size = "small")
    message_to_screen("Press C to play or Q to quit", black, 180, size = "small")

    while intro:
        for event in pygame.event.get(): ### choice to exit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                    game_running()


                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(40)

############# S T A R T I N G   T H E   G A M E ##########################
pygame.init()
gameIntro()

pygame.quit()
quit()


gameLoop()