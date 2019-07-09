import pygame
import random


class Unit:
    """
    class for object in the game world, like units, enemies or projectiles
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
        self.moveRandom()

    def collide(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True

        return false

    def __str__(self):
        return "at {0} {1}".format(self.x, self.y)

    def moveRandom(self):
        if random.randint(0, 10) > 9:
            self.last = random.randint(0, 4)

        if self.last == 0:
            self.x = self.x + 1
        elif self.last == 1:
            self.x = self.x - 1
        elif self.last == 2:
            self.y += 1
        elif self.last == 3:
            self.y -= 1
        else:
            pass

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True
