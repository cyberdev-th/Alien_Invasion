import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Classe que gerencia as balas disparadas da nave."""

    def __init__(self, ai_game):
        """Cria um objeto bala(bullet) saindo da posição atual da nave."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)
    
    def update(self):
        """Move a bala na tela."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenha a bala na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)