import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Classe que representa um alienígena invasor."""

    def __init__(self, ai_game):
        """Inicializa o alienígena e o configura."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """Retorna verdadeiro se o alien atingiu a borda."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        """Move o alienígena para a direita ou esquerda."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x