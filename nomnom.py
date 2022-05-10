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
Eel.set_colorkey((255,255,255))
Eel2 = pygame.image.load('eelface2.png') #load your spritesheet
Eel2.set_colorkey((255,255,255))

fishy = pygame.image.load('fishy.png')
fishy.set_colorkey((255,255,255))
Back = pygame.image.load('background.png')

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3
Px= 800 #xpos of player
Py= 800 #ypos of player
Px2 = 200
Py2 = 200
score = 0
score2 = 0
vx = 0 #x velocity of player
vy = 0 #y velocity of player
vx2 = 0
vy2 = 0
keys = [False, False, False, False] #this list holds whether each key has been pressed
second = [False, False, False, False]

frameWidth = 50
frameHeight = 50
RowNum = 2
frameNum = 0
RowNum2 = 0
frameNum2 = 0

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

print('how fest u trynna go famalam 1-5')
n = (int(input()))

while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS

#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)


#Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            elif event.key == pygame.K_UP:
                keys[UP]=True
            elif event.key == pygame.K_DOWN:
                keys[DOWN]=True
            if event.key == pygame.K_a:
                second[LEFT]=True
            elif event.key == pygame.K_d:
                second[RIGHT]=True
            elif event.key == pygame.K_w:
                second[UP]=True
            elif event.key == pygame.K_s:
                second[DOWN]=True
           
        if event.type == pygame.KEYUP: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
            elif event.key == pygame.K_UP:
                keys[UP]=False
            elif event.key == pygame.K_DOWN:
                keys[DOWN]=False
            if event.key == pygame.K_a:
                second[LEFT]=False
            elif event.key == pygame.K_d:
                second[RIGHT]=False
            elif event.key == pygame.K_w:
                second[UP]=False
            elif event.key == pygame.K_s:
                second[DOWN]=False
                
    
    
    #physics section--------------------------------------------------------------------
    
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-n
        vy=0
        RowNum = 2
        frameNum = 0
        direction = LEFT
        
    #Right Movement
    elif keys[RIGHT]==True:
        vx=n
        vy=0
        RowNum = 0
        frameNum = 0
        direction = RIGHT
    
      #JUMPING  
    if keys[UP]==True:
        vy=-n
        vx=0
        RowNum = 1
        frameNum = 0
        direction = UP
        
      #DOWN
    if keys[DOWN]==True:
        vy=+n
        vx=0
        RowNum = 3
        frameNum = 0
        direction = DOWN
    
    #LEFT MOVEMENT
    if second[LEFT]==True:
        vx2=-n
        vy2=0
        RowNum2 = 2
        frameNum2 = 0
        direction2 = LEFT
        
    #Right Movement
    elif second[RIGHT]==True:
        vx2=n
        vy2=0
        RowNum2 = 0
        frameNum2 = 0
        direction2 = RIGHT
    
      #JUMPING  
    if second[UP]==True:
        vy2=-n
        vx2=0
        RowNum2 = 1
        frameNum2 = 0
        direction2 = UP
        
      #DOWN
    if second[DOWN]==True:
        vy2=+n
        vx2=0
        RowNum2 = 3
        frameNum2 = 0
        direction2 = DOWN
    #update player position
    Px+=vx 
    Py+=vy
    Px2+=vx2
    Py2+=vy2
    
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
        
    elif CircleCollision(num,Px2, Py2,num1, s)==True:
        num = random.randrange(1, 800)
        num1 = random.randrange(1, 800)
        c1 = random.randrange(1, 255)
        c2 = random.randrange(1, 255)
        c3 = random.randrange(1, 255)
        s = random.randrange(10, 21)
        frameNum2 += 1
        score2 += 1
#player 1 warp zone
    if Px < 0:
        Px=999
    if Px > 999:
        Px=0
    if Py < 0:
        Py=999
    if Py > 999:
        Py=0
#player 2 warp zone        
    if Px2 < 0:
        Px2=999
    if Px2 > 999:
        Px2=0
    if Py2 < 0:
        Py2=999
    if Py2 > 999:
        Py2=0   
    #Render Section ---------------------------
    screen.fill((0,0,255))
    screen.blit(Back, (0,0), (0,0,1000,1000))
    font = pygame.font.Font(None, 74)
    text = font.render(str(score),1, (0, 255, 0))
    screen.blit(text, (750, 10))
    text = font.render(str(score2),1, (0, 255, 0))
    screen.blit(text, (250, 10))
    screen.blit(fishy,(num, num1,25,25))
    screen.blit(Eel, (Px, Py), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    screen.blit(Eel2, (Px2, Py2), (frameWidth*frameNum2, RowNum2*frameHeight, frameWidth, frameHeight))    


    pygame.display.flip()

pygame.quit()
