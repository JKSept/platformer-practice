from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join


class Game:
    def __init__(self):
        pg.init()

        # Set display surface
        self.display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pg.display.set_caption('Platformer')

        # Set up Clock
        self.clock = pg.time.Clock()

        # Level set up
        self.tmx_maps = {0: load_pygame(join('data', 'levels', 'omni.tmx'))}
        self.current_stage = Level(self.tmx_maps[0])


    # Main game loop
    def run(self):
        while True:
            dt = self.clock.tick(60) / 1000
            print(dt)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            # Game logic flow
            self.current_stage.run(dt)

            pg.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()








