import pygame
import sys

from settings import *
from player import Player
from enemy import Enemy
from coin import Coin


class Game:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont("Arial", 30)
        self.big_font = pygame.font.SysFont("Arial", 60)

        self.state = MENU

        self.reset_game()

    # ------------------------------------

    def reset_game(self):

        self.player = Player()

        self.score = 0

        self.coins = []

        for i in range(COIN_COUNT):
            self.coins.append(Coin())

        self.enemies = []

        for i in range(ENEMY_COUNT):
            self.enemies.append(Enemy())

    # ------------------------------------

    def run(self):

        while True:

            if self.state == MENU:
                self.menu()

            elif self.state == PLAYING:
                self.play()

            elif self.state == WIN:
                self.win()

            elif self.state == GAME_OVER:
                self.game_over()

    # ------------------------------------

    def menu(self):

        while self.state == MENU:

            self.clock.tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:

                        self.reset_game()
                        self.state = PLAYING

                    if event.key == pygame.K_ESCAPE:

                        pygame.quit()
                        sys.exit()

            self.screen.fill(GREEN)

            title = self.big_font.render(
                "CAÇA AO TESOURO",
                True,
                WHITE
            )

            self.screen.blit(
                title,
                (
                    WIDTH // 2 - title.get_width() // 2,
                    80
                )
            )

            txt = self.font.render(
                "ENTER - Jogar",
                True,
                WHITE
            )

            self.screen.blit(
                txt,
                (
                    WIDTH // 2 - txt.get_width() // 2,
                    220
                )
            )

            txt = self.font.render(
                "ESC - Sair",
                True,
                WHITE
            )

            self.screen.blit(
                txt,
                (
                    WIDTH // 2 - txt.get_width() // 2,
                    270
                )
            )

            txt = self.font.render(
                "Movimento: WASD ou Setas",
                True,
                WHITE
            )

            self.screen.blit(
                txt,
                (
                    WIDTH // 2 - txt.get_width() // 2,
                    350
                )
            )

            txt = self.font.render(
                "Colete todas as moedas",
                True,
                WHITE
            )

            self.screen.blit(
                txt,
                (
                    WIDTH // 2 - txt.get_width() // 2,
                    390
                )
            )

            txt = self.font.render(
                "Evite os monstros",
                True,
                WHITE
            )

            self.screen.blit(
                txt,
                (
                    WIDTH // 2 - txt.get_width() // 2,
                    430
                )
            )

            pygame.display.flip()



                # ------------------------------------

    def play(self):

        while self.state == PLAYING:

            self.clock.tick(FPS)

            # -----------------------------
            # EVENTOS
            # -----------------------------

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        self.state = MENU

            # -----------------------------
            # ATUALIZA JOGADOR
            # -----------------------------

            self.player.update()

            # -----------------------------
            # ATUALIZA INIMIGOS
            # -----------------------------

            for enemy in self.enemies:
                enemy.update()

            # -----------------------------
            # COLISÃO COM INIMIGOS
            # -----------------------------

            for enemy in self.enemies:

                if self.player.rect.colliderect(enemy.rect):

                    self.player.hit()

                    pygame.time.delay(300)

                    if self.player.lives <= 0:
                        self.state = GAME_OVER

            # -----------------------------
            # COLETA DAS MOEDAS
            # -----------------------------

            for coin in self.coins:

                if coin.collected:
                    continue

                if self.player.rect.colliderect(coin.rect):

                    coin.collect()

                    self.score += 1

            # -----------------------------
            # VITÓRIA
            # -----------------------------

            if self.score >= COIN_COUNT:

                self.state = WIN

            # -----------------------------
            # DESENHA A TELA
            # -----------------------------

            self.screen.fill(GREEN)

            # moedas

            for coin in self.coins:
                coin.draw(self.screen)

            # inimigos

            for enemy in self.enemies:
                enemy.draw(self.screen)

            # jogador

            self.player.draw(self.screen)

            # -----------------------------
            # HUD
            # -----------------------------

            pygame.draw.rect(
                self.screen,
                GRAY,
                (0, 0, WIDTH, 55)
            )

            score = self.font.render(
                f"Moedas: {self.score}/{COIN_COUNT}",
                True,
                WHITE
            )

            self.screen.blit(score, (20, 12))

            lives = self.font.render(
                f"Vidas: {self.player.lives}",
                True,
                WHITE
            )

            self.screen.blit(lives, (250, 12))

            pygame.display.flip()
                # ------------------------------------

    def win(self):

        while self.state == WIN:

            self.clock.tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        self.reset_game()
                        self.state = PLAYING

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.screen.fill((20, 120, 20))

            title = self.big_font.render(
                "VOCÊ VENCEU!",
                True,
                WHITE
            )

            self.screen.blit(
                title,
                (
                    WIDTH // 2 - title.get_width() // 2,
                    140
                )
            )

            txt = self.font.render(
                "Parabéns! Você coletou todas as moedas!",
                True,
                WHITE
            )

            self.screen.blit(
                txt,
                (
                    WIDTH // 2 - txt.get_width() // 2,
                    250
                )
            )

            txt = self.font.render(
                "ENTER - Jogar novamente",
                True,
                WHITE
            )

            self.screen.blit(
                txt,
                (
                    WIDTH // 2 - txt.get_width() // 2,
                    320
                )
            )

            txt = self.font.render(
                "ESC - Sair",
                True,
                WHITE
            )

            self.screen.blit(
                txt,
                (
                    WIDTH // 2 - txt.get_width() // 2,
                    370
                )
            )

            pygame.display.flip()

    # ------------------------------------

    def game_over(self):

        while self.state == GAME_OVER:

            self.clock.tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        self.reset_game()
                        self.state = PLAYING

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.screen.fill((120, 20, 20))

            title = self.big_font.render(
                "GAME OVER",
                True,
                WHITE
            )

            self.screen.blit(
                title,
                (
                    WIDTH // 2 - title.get_width() // 2,
                    140
                )
            )

            txt = self.font.render(
                "Você perdeu todas as vidas.",
                True,
                WHITE
            )

            self.screen.blit(
                txt,
                (
                    WIDTH // 2 - txt.get_width() // 2,
                    250
                )
            )

            txt = self.font.render(
                "ENTER - Jogar novamente",
                True,
                WHITE
            )

            self.screen.blit(
                txt,
                (
                    WIDTH // 2 - txt.get_width() // 2,
                    320
                )
            )

            txt = self.font.render(
                "ESC - Sair",
                True,
                WHITE
            )

            self.screen.blit(
                txt,
                (
                    WIDTH // 2 - txt.get_width() // 2,
                    370
                )
            )

            pygame.display.flip()
