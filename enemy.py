import pygame
import random
from settings import *

class Enemy:

    def __init__(self):

        self.size = ENEMY_SIZE

        # Evita nascer muito perto das bordas
        self.rect = pygame.Rect(
            random.randint(60, WIDTH - 60),
            random.randint(60, HEIGHT - 60),
            self.size,
            self.size
        )

        # Velocidade aleatória
        self.speed_x = random.choice([-1, 1]) * random.randint(2, ENEMY_SPEED)
        self.speed_y = random.choice([-1, 1]) * random.randint(2, ENEMY_SPEED)

        self.color = RED

    def update(self):

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Colisão com as paredes

        if self.rect.left <= 0:
            self.rect.left = 0
            self.speed_x *= -1

        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            self.speed_x *= -1

        if self.rect.top <= 0:
            self.rect.top = 0
            self.speed_y *= -1

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed_y *= -1

    def respawn(self):
        """
        Move o inimigo para outro ponto aleatório.
        Será útil em versões futuras.
        """

        self.rect.x = random.randint(60, WIDTH - 60)
        self.rect.y = random.randint(60, HEIGHT - 60)

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            self.color,
            self.rect,
            border_radius=8
        )