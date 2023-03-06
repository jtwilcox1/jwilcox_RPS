# file created by JT Wilcox

# import libraries

from time import sleep

from random import randint 

import pygame as pg
# this will display the text in pygame
import pygame
pygame.font.init()
screen = pygame.display.set_mode((900,700))
textfont = pygame.font.SysFont("monospace",40)

running = True
while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
    textTBD = textfont.render("Choose Rock Paper or Scissors", 1,(255,255,255))
    screen.blit(textTBD,(100,100))
    textTBD = textfont.render("You Win", 1,(255,255,255))
    screen.blit(textTBD,(100,500))
    textTBD = textfont.render("You Lose", 1,(255,255,255))
    screen.blit(textTBD,(400,500))
    textTBD = textfont.render("Tie", 1,(255,255,255))
    screen.blit(textTBD,(700,500))

   
pygame.display.update()

            
pygame.quit()

import os 

# setup asset folders - images and sounds as needed
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings 
WIDTH = 900
HEIGHT = 700
FPS = 30

# define colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (225, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock Paper Scissors...")
clock = pg.time.Clock()
rock_image = pg.image.load(os.path.join(game_folder, 'rock.png')).convert()
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.png')).convert()
paper_image = pg.image.load(os.path.join(game_folder, 'paper.png')).convert()
# this gets the geometry of the image
rock_rect = rock_image.get_rect()
scissors_rect = scissors_image.get_rect()
paper_rect = paper_image.get_rect()


# this will divide the inital starting coordinate of the picture by 2
paper_rect.x = WIDTH/1.5
scissors_rect.x = WIDTH/3
    
    

pygame.display.update()

            
pygame.quit()

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock Paper Scissors...")
clock = pg.time.Clock()
rock_image = pg.image.load(os.path.join(game_folder, 'rock.png')).convert()
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.png')).convert()
paper_image = pg.image.load(os.path.join(game_folder, 'paper.png')).convert()
# this gets the geometry of the image
rock_rect = rock_image.get_rect()
scissors_rect = scissors_image.get_rect()
paper_rect = paper_image.get_rect()


# this will divide the inital starting coordinate of the picture by 2
paper_rect.x = WIDTH/1.5
scissors_rect.x = WIDTH/3



running = True 
while running: 
    clock.tick(FPS)
# example: head turn left VR turn left
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP: 
            print(pg.mouse.get_pos())
            # position of coordinates
            mouse_coords = pg.mouse.get_pos()
            print(mouse_coords)
            print(mouse_coords[0])
            print(mouse_coords[1])
            print(rock_rect.collidepoint(mouse_coords))
            # if you click on the coordinates where the rock image it will print "this the rock"
            if rock_rect.collidepoint(mouse_coords) == True:
                print("this is the rock")
                userchoice = "rock"
                # same thing for paper
            elif paper_rect.collidepoint(mouse_coords) == True:
                print("this is paper")
                # same for scissors
            elif scissors_rect.collidepoint(mouse_coords) == True:
                print("this is scissors")
                # if you do not click on any image it will print "this is nothing"
            else:
                print("this is nothing")
            
            if rock_rect.collidepoint(mouse_coords) == True:
                print("you chose rock")
            elif paper_rect.collidepoint(mouse_coords) == True:
                print("you chose paper")
            elif scissors_rect.collidepoint(mouse_coords) == True:
                print("you chose scissors")


 
            # these are the coordinates of the rock image
            # if mouse_coords[0] <= 299 and mouse_coords[1] <= 168:
            #     # print(my_image_rect.collidepoint(mouse_coords))
            #     print("this is the rock")

    # get input from player

    # update 
    # these will shift the starting point of the image on the x or y intercept
    # rock_rect.y += 1
    # paper_rect.y += 1
    # scissors_rect.x += 1
    # scissors_rect.y += 1
    
    # draw 
# background is black
# these will actually make the images appear in pygame
    screen.fill(BLACK)
    screen.blit(rock_image, rock_rect)
    screen.blit(paper_image, paper_rect)
    screen.blit(scissors_image, scissors_rect)

    pg.display.flip()

pg.quit()

# libraries
# suspense
# # libraries, import sleep to give pause give pause in between
from time import sleep
# random pseudo random
# randint=number generator (psuedo random)
from random import randint
# the computer chooses rock paper scissors in the form if 123
# the names that display for 123 in the terminal
# anything with "" are strings, strings behave like lists with index 
playing = True
choices = ["rock","paper","scissors"]

# print("Let's play: " + str(choices))
# will print "lets play" and choose either rock paper or scissors
# print("lets play: " + str(choices0))
print("Let's play: ", choices[0], choices[1], choices[2])
# the computer tells us to choose rock paper or scissors
def get_userchoice():
    global user_choice
    user_choice = input("Choose rock paper or scissors...")

def cpu_choice():
# prints the computer has chosen something from random integer tool
# return "The computer has chosen " + choices0[randint(0,2)]
# displays the choice
    return choices[randint(0,2)]

def wanna_play():
    response = input("do you want to play rock paper scissors?")
    if response == "no":
        return False
    elif response == "yes":
        print("W!!!")
        return True
    else:
        print("need more input....")
# game, catdog, battle, start, rock_paper_scissors
def rps():
    wanna_play()
    get_userchoice()
    cpu = cpu_choice()
    print("The computer chose", cpu)
    if user_choice == cpu:
        print("Tie!!")
    elif user_choice == "rock":
        if cpu == "scissors":
            print("Winner!!!")
        elif cpu == "paper":
            print("You lost pal")
    elif user_choice =="paper":
        if cpu == "rock":
            print("Winner!!!")
        elif cpu == "scissors":
            print("you lost pal")
    elif user_choice == "scissors":
        if cpu == "rock":
            print("you lost pal")
        elif cpu == "paper":
            print("Winner!!!")

    else:
        print("An error of type 0affedf0")

# while True:
#     playing = wanna_play()
#     print("playing is", playing)
#     if playing == False:
#         break
#     else:
#         get_userchoice()
#         compare()
rps()


