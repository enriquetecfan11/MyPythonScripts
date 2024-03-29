import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('D1.png'), pygame.image.load('D2.png'), pygame.image.load('D3.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png')]
bg = pygame.image.load('bg.png')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

score = 0


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.health = 10
        self.visible = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//100], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//100], (self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(char, (self.x,self.y))

        self.hitbox = (self.x + 1, self.y + -2, 40, 40)

        pygame.draw.rect(win, (255,0,0), self.hitbox,2) # To draw the hit box around the player

        pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10)) # Heatlh Bar

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('Player Hit')

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

class enemy(object):
    walkRight = [pygame.image.load('E2.png')]
    walkLeft = [pygame.image.load('E1.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.health = 10 
        self.visible = True
        self.isJump = False
        self.jumpCount = 10

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//100], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//100], (self.x,self.y))
            self.walkCount += 1
        
        pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) # HitBox

        pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10)) # Heatlh Bar

        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        
        if self.walkCount > 10:
            self.jumpCount

        self.hitbox = (self.x + 1, self.y + -2, 40, 40)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
    
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('Enemy Hit')

def redrawGameWindow():
    win.blit(bg, (0,0))
    goblin.draw(win)
    man.draw(win)

    #for bullet in bullets:
    #    bullet.draw(win)

    text = font.render("Score: " + str(score), 1, (0,0,10)) # Arguments are: text, anti-aliasing, color
    win.blit(text, (100, 10))

    walkcount = man.walkCount
    text = font.render("Count: " + str(walkcount), 1, (0,0,10)) # Arguments are: text, anti-aliasing, color
    win.blit(text, (390, 10))

    jumpcount = man.jumpCount 
    text = font.render("Jump: " + str(jumpcount), 1, (0,0,0))
    win.blit(text, (250, 10))
    
    pygame.display.update()


#mainloop
man = player(200, 410, 64,64)
font = pygame.font.SysFont("comicsans", 30, True)
goblin = enemy(100, 410, 64, 64, 300)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                score += 1 # NEW CODE
                bullets.pop(bullets.index(bullet))
                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        print("Disparando !!")
        #if man.left:
            #pygame.image.load("gun.png")
        #    facing = -1
        #else:
        #    facing = 1
            
        #if len(bullets) < 5:
        #    bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()