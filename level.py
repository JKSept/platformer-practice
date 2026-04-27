from settings import *
from sprites import Sprite


class Level:
    def __init__(self, tmx_map):
        self.display_surface = pg.display.get_surface()

        # Group setup
        self.all_sprites = pg.sprite.Group()

        # Map setup
        self.setup(tmx_map)


    def setup(self, tmx_map):
        for x, y, surface in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surface, self.all_sprites)


    def run(self):
        self.display_surface.fill('gray')
        self.all_sprites.draw(self.display_surface)
