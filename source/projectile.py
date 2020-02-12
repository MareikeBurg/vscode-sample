import pygame
import random
import math

from unit import Unit


class Projectile(Unit):
    """
    class for  projectiles
    """

    # collison works circual, r
    def __init__(self, x, y, sprite, window, health, collisonradius, target: (int, int), scale):
        Unit.__init__(self, x, y, sprite, window, health, collisonradius, scale)

        self.speed = 2
        self.damage = 5

        self.targetx = target[0]
        self.targety = target[1]

        # each tick t x and y values are increadsed by this valeus
        self.stepx, self.stepy = self.aim()

    # draws moves and updates
    def update(self):
        self.window.blit(self.sprite, (self.x, self.y))
        # self.win.blit(self.img, (self.x, self.y))
        # self.moveRandom()

        # testing hitboxes
        pygame.draw.circle(
            self.window, (255, 0, 0), (int(self.x), int(self.y)), self.collisonradius
        )

        self.move()

    def aim(self):
        diffx, diffy = abs(self.x - self.targetx), abs(self.y - self.targety)
        alpha = math.atan(diffx / diffy)

        dirx, diry = (-1 if self.x > self.targetx else 1, -1 if self.y > self.targety else 1)

        return dirx * math.sin(alpha) * self.speed, diry * math.cos(alpha) * self.speed

    def move(self):
        self.x += self.stepx
        self.y += self.stepy

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
