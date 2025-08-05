import sys
import pygame

class AlienInvasion:
    """
    Classe que gerencia todo o jogo e seus recursos.
    """

    def __init__(self):
        """Inicializa o jogo e cria seus recursos necessários."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((800,400))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = (230,230,230)

    def run_game(self):
        """Inicia o loop principal do jogo."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            
            # torna o desenho de tela mais recente visível
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()