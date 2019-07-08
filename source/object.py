import pygame


class Object:
    """
    class for object in the game world, like units, enemies or projectiles
    """

    def __init__(self, x, y, spritenumer):
        self.x = x
        self.y = y
        # only exsiting values at the moment
        self.width = 32
        self.height = 48
        self.health = 1
        self.spritenumber = spritenumer

    # draws moves and updates
    def update(self, win):

        self.current_animation
        self.img = self.imgs[self.current_animation]
        win.blit(self.img, (self.x, self.y))
        self.move(1)

    def collide(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True

        return false

    def move(self, dir):

        pass

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True
