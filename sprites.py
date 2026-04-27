from settings import *


class Sprite(pg.sprite.Sprite):
    def __init__(self, pos, surface, groups):
        super().__init__(groups)

        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill('black')

        self.rect = self.image.get_frect(topleft=pos)