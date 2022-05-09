import pygame
import random
import math
pygame.init()  
pygame.display.set_caption("platformer")  # sets the window title
screen = pygame.display.set_mode((1000, 1000))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop
red = (255,0,0)


Eel = pygame.image.load('eelface.png') #load your spritesheet
Eel.set_colorkey((255,255,255)) #this makes bright pink (255, 0, 255) transparent (sort of)
fishy = pygame.image.load('fishy.png')
fishy.set_colorkey((255,255,255))
Back = pygame.image.load('background.png')

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3
Px= 200 #xpos of player
Py= 200 #ypos of player
score = 0
score2 = 0
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed

frameWidth = 50
frameHeight = 50
RowNum = 0
frameNum = 0
def CircleCollision(x1,x2,y1,y2, radius):
    if (math.sqrt((x2 - x1)**2 + (y2- y1)**2))<radius:
        return True
    else:
        return False

#set up first circle's position and color and size
num = random.randrange(1, 800)
num1 = random.randrange(1, 800)
c1 = random.randrange(1, 255)
c2 = random.randrange(1, 255)
c3 = random.randrange(1, 255)
s = random.randrange(10, 100)
#set up variable to hold mouse position
xpos=0
ypos=0
mousePos = (xpos, ypos)


while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS

#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)


#Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_a:
                keys[LEFT]=True
            elif event.key == pygame.K_d:
                keys[RIGHT]=True
            elif event.key == pygame.K_w:
                keys[UP]=True
            elif event.key == pygame.K_s:
                keys[DOWN]=True
           
        if event.type == pygame.KEYUP: #keyboard input
            if event.key == pygame.K_a:
                keys[LEFT]=False
            elif event.key == pygame.K_d:
                keys[RIGHT]=False
            elif event.key == pygame.K_w:
                keys[UP]=False
            elif event.key == pygame.K_s:
                keys[DOWN]=False
                
    if event.type == pygame.MOUSEBUTTONDOWN:#CLICK
        mousePos = event.pos

    if event.type == pygame.MOUSEBUTTONUP:#release
        draw = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
       
    if event.type == pygame.QUIT: #close game window
        break        
 
    #physics/movement section#LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        vy=0
        RowNum = 2
        frameNum = 0
        direction = LEFT
        
    elif keys[RIGHT]==True:
        vx=3
        vy=0
        RowNum = 0
        frameNum = 0
        direction = RIGHT
    

        
      #JUMPING  
    if keys[UP]==True:
        vy=-3
        vx=0
        RowNum = 1
        frameNum = 0
        direction = UP

        
      #DOWN
    elif keys[DOWN]==True:
        vy = 3
        vx=0
        RowNum = 3
        frameNum = 0
        direction = DOWN
    

    #update player position
    Px+=vx 
    Py+=vy
    
    #try to call the function here, use the new variables
    #(put the call inside an if statement, and only get new points for the circle when it's clicked on)
    if CircleCollision(num,Px, Py,num1, s)==True:
        
        num = random.randrange(1, 800)
        num1 = random.randrange(1, 800)
        c1 = random.randrange(1, 255)
        c2 = random.randrange(1, 255)
        c3 = random.randrange(1, 255)
        s = random.randrange(10, 21)

        frameNum += 1
        score += 1
        score2 += 1

    if Px < 0:
        Px=999
    if Px > 999:
        Px=0
    if Py < 0:
        Py=999
    if Py > 999:
        Py=0
    #Render Section ---------------------------
    screen.fill((0,0,255))
    screen.blit(Back, (0,0), (0,0,1000,1000))
    font = pygame.font.Font(None, 74)
    text = font.render(str(score),1, (0, 255, 0))
    text2 = font.render(str(score),1, (0,255,0))
    screen.blit(text2, (750, 10)) 
    screen.blit(text, (250, 10))
    screen.blit(fishy,(num, num1,25,25))
    screen.blit(Eel, (Px, Py), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))    


    pygame.display.flip()

pygame.quit()

