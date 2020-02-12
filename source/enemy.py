import pygame
import random
from unit import Unit


class Enemy(Unit):
    """
    class for object in the game world, like units, enemies or projectiles
    """

    def __init__(self, x, y, sprite, window, health, collisonradius, scale):
        Unit.__init__(self, x, y, sprite, window, health, collisonradius, scale)

        # new movment algorithm
        self.last = random.randint(0, 3)

    # draws moves and updates
    def update(self):
        self.window.blit(self.sprite, (self.x, self.y))
        # self.win.blit(self.img, (self.x, self.y))
        # self.moveRandom()
        # testing hitboxes
        pygame.draw.circle(
            self.window, (255, 0, 0), (int(self.x), int(self.y)), self.collisonradius
        )

    """
    def collide(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True

        return false
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

    def hit(self, projectile):

        self.health -= projectile.damage

        if self.health <= 0:
            return True
