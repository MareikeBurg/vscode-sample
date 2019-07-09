import pygame
import random

from unit import Unit


class Projectile(Unit):
    """
    class for  projectiles
    """

    # collison works circual, r
    def __init__(self, x, y, sprite, window, collisonradius):
        self.x = x
        self.y = y
        # only exsiting values at the moment
        self.width = 32
        self.height = 48
        self.collisonradius = collisonradius
        self.centerxoffset = 16
        self.centeryoffset = 16

        self.health = 3
        self.sprite = sprite
        self.window = window

        # new movment algorithm
        self.last = random.randint(0, 3)
        self.damage = 5

    # draws moves and updates
    def update(self):
        self.window.blit(self.sprite, (self.x, self.y))
        # self.win.blit(self.img, (self.x, self.y))
        # self.moveRandom()
        self.move()

    def move(self):
        self.y += 1

    """

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
    """

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True
