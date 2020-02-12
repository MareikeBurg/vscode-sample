import pygame
from generator import Generator


class Field:
    def __init__(self, screen, scale, tile_list):
        self.tile_list = tile_list
        self.screen = screen
        self.gen = Generator()
        self.layout = self.gen.custom(width=16, height=9, allowedTiles=[1, 2, 3, 4])
        self.x, self.y = 16, 9
        self.scale = scale

    def draw(self, x: int, y: int, tiletype):

        self.screen.blit(self.tile_list[tiletype], (x, y))
        """
        if tiletype == 0:
            self.screen.blit(self.tile_list[0], (x, y))
        elif tiletype == 1:
            self.screen.blit(self.tile_list[1], (x, y))
        elif tiletype == 2:
            self.screen.blit(self.tile_list[5], (x, y))
        elif tiletype == 3:
            self.screen.blit(self.tile_list[6], (x, y))
        """

    # TODO sprites sind nicht hexagonal, oben fehlen zwei reihen pixel, sieht unschön aus
    def drawall(self):
        for i in range(self.x):
            for j in range(self.y):
                # x and y position, 3/4 tilesize is offset in both direction, y is set down 1/2 tilesize at each second row
                # if(self.layout[i][j])
                self.draw(
                    16 * 5 + i * 24 * self.scale,
                    9 * 5 + j * 32 * self.scale + (i % 2) * 16 * self.scale - 1 * j * self.scale,
                    self.layout[i][j],
                )

