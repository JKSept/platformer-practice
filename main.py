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

        # --
        self.tmx_maps = {0: load_pygame(join('data', 'levels', 'omni.tmx'))}
        self.current_stage = Level(self.tmx_maps[0])




    # Main game loop
    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            # Game logic flow
            self.current_stage.run()

            pg.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()








