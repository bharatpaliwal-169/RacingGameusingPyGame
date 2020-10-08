import pygame
import time
import random
#initailize the game
pygame.init()

#Display SetUp
display_width = 950
display_height = 700
car_width = 108
#colors 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
myBlack = (24,24,24)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A Bit Racey')

#clock
clock = pygame.time.Clock()

#item
carImg = pygame.image.load('car.jpeg')


#FUNCTIONS
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf , TextRect = text_objects("A Bit Racey",largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(15)


def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Score: " + str(count),True,black)
    gameDisplay.blit(text,(0,0))

def things(tx,ty,thing_width,thing_height,color):
    pygame.draw.rect(gameDisplay,color,[tx,ty,thing_width,thing_height])


def text_objects(text,font):
    textSurface = font.render(text,True,red)
    return textSurface , textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf , TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

    time.sleep(2)
    gameLoop()

def crash():
    message_display("You Crashed!!")

def gameLoop():
    x = (display_width * 0.45)
    y = (display_height * 0.67)

    x_change = 0
    #things parameters
    
    thing_starty = -600
    t_speed = 3
    thing_width = 120
    thing_height = 120
    thing_startx = random.randrange( 0 ,display_width - thing_width)

    dodged = 0
    #crasher....
    gameExit = False

    #event handler
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -15
                elif event.key == pygame.K_RIGHT:
                    x_change = 15
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
        x += x_change 

        gameDisplay.fill(white)
        #things() -> tx,ty,thing_width,thing_height
        things(thing_startx,thing_starty,thing_width,thing_height,myBlack)
        thing_starty += t_speed
        car(x,y)
        things_dodged(dodged)
        #boundary conditions
        if x > (display_width-car_width) or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width-thing_width)
            dodged += 1
            t_speed += 1
        if y < thing_starty + thing_height:
            # print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                # print('x crossover')
                crash()

        pygame.display.update()
        #FPS 
        clock.tick(150)          
#start
game_intro()
gameLoop()
#exit
pygame.quit()
quit()