import pygame

class Enemy:
imgs = []

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = 1
        self.img = None
        #cycle trough diffrent animations
        self.current_animation = 0

    #draws moves and updates
    def update(self,win):
        
        self.current_animation
        self.img = self.imgs[self.current_animation]
        win.blit(self.img, (self.x, self.y))
        self.move(1)

    def collide(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y+self.height and Y >= self.y:
                return True

        return false

    def move(self, dir):

        pass

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True