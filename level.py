from settings import *
from sprites import Sprite
from player import Player


class Level:
    def __init__(self, tmx_map):
        self.display_surface = pg.display.get_surface()

        # Sprite Group setup
        self.all_sprites = pg.sprite.Group()
        self.collision_sprites = pg.sprite.Group()

        # Map setup
        self.setup(tmx_map)


    def setup(self, tmx_map):
        for x, y, surface in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surface, (self.all_sprites, self.collision_sprites))

        for obj in tmx_map.get_layer_by_name('Objects'):
            if obj.name == "player":
                Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)
                



    def run(self, dt):
        # update all sprites
        

        self.display_surface.fill('gray')
        self.all_sprites.update(dt)
        # draw all sprites
        self.all_sprites.draw(self.display_surface)
