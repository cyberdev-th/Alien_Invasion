class GameStats:
    """Rastreia estatísticas do jogo Alien Invasion."""

    def __init__(self, ai_game):
        """Inicializa as estatísticas."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit