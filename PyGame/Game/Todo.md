
## TODO
 - Enemy Player // Done
 - Health Bar // Done
 - Score // Done
 - WalkCount (Subirlo para andar mas) // Done

## Para hacer que salte el jugador
        if self.walkCount == 30:
            if self.jumpCount == -10:
                neg = -1
                self.jumpCount = -10
            if self.jumpCount < 0:
                neg = +1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
        
        if self.walkCount == 32:
            self.jumpCount = False
            self.jumpCount = -10


## Para hacer que se mueva el jugador
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


##

if self.jumpCount == -10:
                neg = -1
                self.jumpCount = -10

            if self.jumpCount < 0:
                neg = 1                               # Altura del salto
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1