from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)

        # Player setup
        self.image = pg.Surface((48, 56))
        self.image.fill('green')
        # rects
        self.rect = self.image.get_frect(topleft=pos)
        self.old_rect = self.rect.copy()

        # Movement setup
        self.direction = vector()
        self.speed = 200
        self.gravity = 1000

        # Collision setup
        self.collision_sprites = collision_sprites
        

    # Inputs
    def input(self):
        keys = pg.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pg.K_w]:
            input_vector.y -= 1
            
        if keys[pg.K_s]:
            input_vector.y += 1
            
        self.direction.x = input_vector.normalize().x if input_vector else input_vector.x

    # Movement 
    def move(self, dt):
        # horizontal
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        # vertical
        self.direction.y += self.gravity / 2 * dt
        self.rect.y += self.direction.y * dt
        self.direction.y += self.gravity / 2 * dt
        self.collision('vertical')


    # Collision
    def collision(self, axis):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if axis == 'horizontal':
                    #left
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                    #right
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                else:
                    # top
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                    # bottom
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                    self.direction.y = 0


    # Update player method
    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)

        