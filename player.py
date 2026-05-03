from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        # Player setup
        self.image = pg.Surface((48, 56))
        self.image.fill('green')
        self.rect = self.image.get_frect(topleft=pos)

        # Movement setup
        self.direction = vector()
        self.speed = 200
        

    # Inputs
    def input(self):
        keys = pg.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pg.K_w]:
            input_vector.y -= 1
            
        if keys[pg.K_s]:
            input_vector.y += 1
            
        if keys[pg.K_d]:
            input_vector.x += 1
           
        if keys[pg.K_a]:
            input_vector.x -= 1
            
        self.direction = input_vector.normalize() if input_vector else input_vector

    # Movement 
    def move(self, dt):
        self.rect.topleft += self.direction * self.speed * dt


    # Update player method
    def update(self, dt):
        self.input()
        self.move(dt)

        