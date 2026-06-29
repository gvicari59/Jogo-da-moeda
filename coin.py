import pygame
import random
from settings import *

class Coin:

    def __init__(self):
        self.size = COIN_SIZE

        self.rect = pygame.Rect(
            random.randint(40, WIDTH - 40),
            random.randint(40, HEIGHT - 40),
            self.size,
            self.size
        )

        self.collected = False

        self.color = YELLOW

    def collect(self):
        """
        Marca a moeda como coletada.
        """
        self.collected = True

    def respawn(self):
        """
        Reaparece em outra posição.
        (Será usado futuramente caso criemos novas fases.)
        """
        self.collected = False

        self.rect.x = random.randint(40, WIDTH - 40)
        self.rect.y = random.randint(40, HEIGHT - 40)

    def draw(self, screen):

        if self.collected:
            return

        pygame.draw.circle(
            screen,
            self.color,
            self.rect.center,
            self.size // 2
        )

        # Brilho da moeda
        pygame.draw.circle(
            screen,
            WHITE,
            (
                self.rect.centerx - 4,
                self.rect.centery - 4
            ),
            3
        )