import pygame
import time
pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('D1.png'), pygame.image.load('D2.png'), pygame.image.load('D3.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png')]
bg = pygame.image.load('bg.png')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

score = 0


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


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
        self.vel = 2
        self.health = 10
        self.visible = True
        self.isJump = False
        self.jumpCount = -10

    def draw(self, win):
        self.move()

        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//500], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//500], (self.x, self.y))
            self.walkCount += 1

        pygame.draw.rect(
            win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))  # HitBox

        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (
            5 * (10 - self.health)), 10))  # Heatlh Bar

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

        if self.walkCount == 30:

            if self.jumpCount == -10:
                neg = -2
                self.jumpCount = -10
                self.y = self.path[1]
                # print(self.y)

        # print(self.jumpCount)

        self.hitbox = (self.x + 1, self.y + -2, 40, 40)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('Enemy Hit')


def redrawGameWindow():
    win.blit(bg, (0, 0))
    goblin.draw(win)

    walkcount = goblin.walkCount
    # Arguments are: text, anti-aliasing, color
    text = font.render("Count: " + str(walkcount), 1, (0, 0, 10))
    win.blit(text, (390, 10))

    jumpcount = goblin.jumpCount
    text = font.render("Jump: " + str(jumpcount), 1, (0, 0, 0))
    win.blit(text, (240, 10))

    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


# mainloop
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
                score += 1  # NEW CODE
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    redrawGameWindow()

pygame.quit()
