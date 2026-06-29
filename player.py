import pygame
from settings import *

class Player:

    def __init__(self):

        self.width = PLAYER_SIZE
        self.height = PLAYER_SIZE

        self.speed = PLAYER_SPEED
        self.lives = PLAYER_LIVES

        # Posição inicial (centro da tela)
        self.start_x = WIDTH // 2 - self.width // 2
        self.start_y = HEIGHT // 2 - self.height // 2

        self.rect = pygame.Rect(
            self.start_x,
            self.start_y,
            self.width,
            self.height
        )

        # Cor temporária (depois será substituída por uma imagem)
        self.color = BLUE

    def update(self):

        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy -= self.speed

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy += self.speed

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx -= self.speed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx += self.speed

        self.rect.x += dx
        self.rect.y += dy

        # Limites da tela
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def hit(self):
        """
        Chamado quando o jogador encosta em um inimigo.
        """

        self.lives -= 1
        self.reset_position()

    def reset_position(self):
        """
        Volta o jogador para o centro da tela.
        """

        self.rect.x = self.start_x
        self.rect.y = self.start_y

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            self.color,
            self.rect,
            border_radius=6
        )