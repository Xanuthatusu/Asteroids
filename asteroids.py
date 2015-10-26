import game,config

class Asteroids(game.Game):
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position, dt):
        pass

    def paint(self, surface):
        pass


def main():
    asteroids = Asteroids(config.TITLE, config.SCREEN_X, config.SCREEN_Y, config.FRAMES_PER_SECOND)
    asteroids.main_loop()


main()
