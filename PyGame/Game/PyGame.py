import pygame
import os

pygame.init()

win = pygame.display.set_mode((500,500))
print(pygame.display.Info)
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('D1.png'), pygame.image.load('D2.png'), pygame.image.load('D3.png')]


walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png')]

bg = pygame.image.load(os.path.join('bg.png')).convert()
#bgX = 0
#bgX2 = bg.get_width()

char = pygame.image.load('standing.png')

x = 50
y = 400
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()

left = False
right = False
walkCount = 0

isJump = False
jumpCount = 10

speed = 30  # NEW

run = True

def redrawGameWindow():
    global walkCount

    #win.blit(bg, (bgX, 0))  # draws our first bg image
    #win.blit(bg, (bgX2, 0))  # draws the seconf bg image
    pygame.display.update()  # updates the screen

    
    win.blit(bg, (0, 0))  
    if walkCount + 1 >= 100:
        walkCount = 0
        
    if left:  
        win.blit(walkLeft[walkCount//100], (x,y))
        walkCount += 1              
    elif right:
        win.blit(walkRight[walkCount//100], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0

    print("Walk Count = ", walkCount)

    pygame.display.update() 


## MAIN LOOP ##

font = pygame.font.SysFont('comicsans', 30, True)
run = True
while run:
    clock.tick(speed)  # NEW
    #bgX -= 2.2  # Move both background images back
    #bgX2 -= 2.2

    #if bgX < bg.get_width() * -1:  # If our bg is at the -width then reset its position
    #    bgX = bg.get_width()
    
    #if bgX2 < bg.get_width() * -1:
    #    bgX2 = bg.get_width()

    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            run = False    
            pygame.quit() 
            quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        left = False
        right = True
        
    else: 
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
    
    
    ##print("Jump Count = ", jumpCount)

    redrawGameWindow() 
    
pygame.quit()