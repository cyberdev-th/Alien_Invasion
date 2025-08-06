class Settings:
    """
    Classe para armazenar todos os valores de configurações do jogo.
    """

    def __init__(self):
        """Inicializa as configurações de uma instância do jogo."""

        # Configurações de tela
        self.screen_width = 800
        self.screen_height = 400
        self.bg_color = (230,230,230)

        # configuração da nave
        self.ship_speed = 2.5

        