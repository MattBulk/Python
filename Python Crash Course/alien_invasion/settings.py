class Settings:

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800

        self.dimensions = (1200, 800)

        self.bg_color = (220, 220, 220)
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3