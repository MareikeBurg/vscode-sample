import pygame
from unit import Unit


class Tower(Unit):
    """
    class for towers
    """

    def __init__(self, x, y, sprite, window):
        self.x = x
        self.y = y
        # only exsiting values at the moment
        self.width = 32
        self.height = 48
        self.health = 1
        self.sprite = sprite
        self.window = window

        # new movment algorithm
        self.last = random.randint(0, 3)

    # draws moves and updates
    def update(self):
        self.window.blit(self.sprite, (self.x, self.y))
        # self.win.blit(self.img, (self.x, self.y))

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True
