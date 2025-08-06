class Settings:
    """
    Classe para armazenar todos os valores de configurações do jogo.
    """

    def __init__(self):
        """Inicializa as configurações de uma instância do jogo."""

        # Configurações de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # valores originais(iniciais)
        self.original_width = self.screen_width
        self.original_height = self.screen_height

        # configuração da nave
        self.ship_speed = 2.5

        