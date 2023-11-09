import pygame
import sounddevice as sd
import numpy as np

class VoiceIndicator:
    def __init__(self, device_index):
        self.audio_input = sd.InputStream(device=device_index, callback=self.audio_callback)
        self.audio_input.start()

        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Voice Indicator")
        self.clock = pygame.time.Clock()
        self.speaking = False

    def audio_callback(self, indata, frames, time, status):
        volume_norm = np.linalg.norm(indata) * 10
        self.speaking = volume_norm > 1  # Determina si se está hablando en función del volumen

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()

            self.screen.fill((0, 0, 0))

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

            radius = self.min_radius + (self.max_radius - self.min_radius) * (np.sin(pygame.time.get_ticks() * self.speed / 1000) + 1) / 2

            self.screen.fill((0, 0, 0))

            pygame.draw.circle(self.screen, self.color, (200, 200), int(radius), self.width)

            pygame.display.flip()
            self.clock.tick(60)

    def stop(self):
        self.audio_input.stop()
        pygame.quit()

if __name__ == "__main__":
    device_index = 33  # Índice del dispositivo de audio que deseas utilizar
    voice_indicator = VoiceIndicator(device_index)
    voice_indicator.run()