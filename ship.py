import pygame

class Ship:
    """Classe que gerencia a nave."""

    def __init__(self, ai_game):
        """Inicializa a nave and configura sua posição inicial."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings

        # carregando a imagem e obtendo seu retângulo
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # posicionando a nave ao centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza a posição da nave baseado em suas flags de movimento"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x

    def blitme(self):
        """Desenha a nave an sua posição atual."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centraliza a nave após uma colisão."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)