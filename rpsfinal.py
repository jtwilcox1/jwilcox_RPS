# File created by: JT Wilcox

 
# import libraries

from time import sleep

from random import randint 

import pygame as pg

import os

game_folder = os.path.dirname(__file__)
print(game_folder)

# These define the height and width of the screen and the FPS
WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
# tuples cant be changed after created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# these are the choices that the player and CPU have to choose from
choices = ["rock", "paper", "scissors"]
# These are the settings of the font displayed in pygame
def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)
# this gives the CPU the option to choose between choice 1,2,or 3. 1 is rock 2 is paper 3 is scissors
def cpu_randchoice():
    choice = choices[randint(0,2)]
    print("The computer chose " + choice)
    return choice
# initate all imported pygame modules
pg.init()
pg.mixer.init()
# the title of the game is Rock, Paper, Scissors...
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors")
clock = pg.time.Clock()
# the image of rock is displayed in pygame
rock_image = pg.image.load(os.path.join(game_folder, 'rock.png')).convert()
rock_image_rect = rock_image.get_rect()
cpu_rock_image_rect = rock_image.get_rect()
# the image of paper is displayed in pygame
paper_image = pg.image.load(os.path.join(game_folder, 'paper.png')).convert()
paper_image_rect = paper_image.get_rect()
cpu_paper_image_rect = paper_image.get_rect()
# the image of scissors is displayed in pygame
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.png')).convert()
scissors_image_rect = scissors_image.get_rect()
cpu_scissors_image_rect = scissors_image.get_rect()

start_screen = True

player_choice = ""
cpu_choice = ""
running = True
# how many frames should pass each second
while running:
    clock.tick(FPS)

    for event in pg.event.get():
        # checks if pygame is still running or not
        if event.type == pg.QUIT:
            running = False
    #    input and human computer interaction. If space bar is clicked game will begin
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                print("Start game")
                start_screen = False

        if event.type == pg.MOUSEBUTTONUP:
            # these are the position of the coordinates
            print(pg.mouse.get_pos()[0])
            
            print(pg.mouse.get_pos()[1])
            
            mouse_coords = pg.mouse.get_pos()

        #    whatever image is clicked the computer knows that this is the weapon you are choosing. 
            print(rock_image_rect.collidepoint(mouse_coords))
            if rock_image_rect.collidepoint(mouse_coords):
                player_choice = "rock"
                # after an image is clicked, the cpu will automaticall choose a random weapon
                cpu_choice = cpu_randchoice()
    
            print(paper_image_rect.collidepoint(mouse_coords))
            if paper_image_rect.collidepoint(mouse_coords):
                player_choice = "paper"
                cpu_choice = cpu_randchoice()
            print (scissors_image_rect.collidepoint(mouse_coords))
            if scissors_image_rect.collidepoint(mouse_coords):
                player_choice = "scissors"
                cpu_choice = cpu_randchoice()      
            
            





    # it shows black before the loop is started
    screen.fill(BLACK)

    # if you hit the space bar, then the images will appear
    if start_screen == True:
        draw_text("Press space to play rock paper scissors", 50, WHITE, WIDTH/2, HEIGHT/10)
        rock_image_rect.x = 2000
        paper_image_rect.x = 2000
        scissors_image_rect.x = 2000
        

    # gives player the chance to choose rock paper or scissors
    if not start_screen and player_choice == "":
        draw_text("Choose your weapon", 40, WHITE, WIDTH/2, HEIGHT/2)
        # coordinates of the images
        rock_image_rect.x = 50
        paper_image_rect.x = 350
        scissors_image_rect.x = 550
        screen.blit(scissors_image, scissors_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(rock_image, rock_image_rect)
        

    # this takes into account every possible outcome and tells the computer what to print when each outcome occurs
    # also the coordinates of the images are moved so that they are not overlaping each other
    if player_choice == "rock":
        if cpu_choice == "rock":
            cpu_rock_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("Tie!", 40, WHITE, WIDTH/2, HEIGHT/2)
    if player_choice == "rock":
        if cpu_choice == "paper":
            cpu_paper_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("You lost!", 40, WHITE, WIDTH/2, HEIGHT/2)
    if player_choice == "rock":
        if cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("You win!!!", 40, WHITE, WIDTH/2, HEIGHT/2)
    if player_choice == "paper":
        if cpu_choice == "paper":
            cpu_paper_image_rect.x = 600
            paper_image_rect.x = 10
            screen.blit(paper_image, paper_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("Tie!", 40, WHITE, WIDTH/2, HEIGHT/2)
    if player_choice == "paper":
        if cpu_choice == "rock":
            cpu_rock_image_rect.x = 500
            paper_image_rect.x = 10
            screen.blit(paper_image, paper_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You win!!!", 40, WHITE, WIDTH/2, HEIGHT/2)
    if player_choice == "paper":
        if cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 500
            paper_image_rect.x = 10
            screen.blit(paper_image, paper_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("You lost!", 40, WHITE, WIDTH/2, HEIGHT/2)
    if player_choice == "scissors":
        if cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 500
            scissors_image_rect.x = 10
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            draw_text("Tie!", 40, WHITE, WIDTH/2, HEIGHT/2)
    if player_choice == "scissors":
        if cpu_choice == "rock":
            cpu_rock_image_rect.x = 500
            scissors_image_rect.x = 10
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You lost!", 40, WHITE, WIDTH/2, HEIGHT/2)
    if player_choice == "scissors":
        if cpu_choice == "paper":
            cpu_paper_image_rect.x = 500
            scissors_image_rect.x = 10
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            draw_text("You win!!!", 40, WHITE, WIDTH/2, HEIGHT/2)
    
    
    # updates the entire surface of display
    pg.display.flip()
# quits from pygame
pg.quit()