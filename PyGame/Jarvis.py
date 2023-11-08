import pygame
import os
import math

class VoiceIndicator:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("J.A.R.V.I.S")
        self.clock = pygame.time.Clock()
        self.speaking = False  # Simulación del atributo speaking

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    os._exit(0)

            self.screen.fill((0,0,0))
            # Si está hablando, hace que la esfera lata más rápido, sea más grande y cambie de color
            if self.speaking:
                self.max_radius = 100
                self.min_radius = 90
                self.speed = 10
                self.color = (255, 140, 0)  # naranja agradable
                self.width = 5
            else:
                self.min_radius = 80
                self.max_radius = 60
                self.speed = 5
                self.color = (0, 255, 255)  # cian
                self.width = 15

            # Calcula el nuevo radio usando una onda sinusoidal para transiciones suaves
            radius = self.min_radius + (self.max_radius - self.min_radius) * (math.sin(pygame.time.get_ticks() * self.speed / 1000) + 1) / 2

            # Limpia la pantalla
            self.screen.fill((0, 0, 0))

            # Dibuja la esfera latente
            pygame.draw.circle(self.screen, self.color, (200, 200), int(radius), self.width)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    voice_indicator = VoiceIndicator()
    voice_indicator.run()
