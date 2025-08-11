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

        # configuração das balas(bullets)
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 8

        # configuração do alienígena
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        