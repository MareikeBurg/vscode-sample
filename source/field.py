import pygame


class Field:
    def __init__(self, screen):
        self.tiles = [["xxa"], ["xxa"], ["aax"]]
        self.tile_list = create_tile_list()
        self.screen = screen

    def draw(self, x, y, tiletype):
        if tiletype == "grass":
            self.screen.blit(self.tile_list[0], (x, y))
        elif tiletype == "forest":
            self.screen.blit(self.tile_list[1], (x, y))


# hardcoded
"""
one tile is 48 pixel high and 32 pixels wide, the spriteset is 6 tiles high and 8 tiles wides. 
Height total 48*6=288, width total 32*8=256

returns a list of all sprites
"""


def create_tile_list():
    tilesize = (48, 32)
    spritesize = (288, 256)
    spritelocation = "assets/sprites/fantasyhextiles_v3.png"
    scale = 4

    image = pygame.image.load(spritelocation).convert_alpha()
    tile_table = []
    # problem with last row, because only one sprit skip for now
    for x in range(0, int(spritesize[0] / tilesize[0]) - 1):
        for y in range(0, int(spritesize[1] / tilesize[1])):
            print(x, y)
            rect = (y * tilesize[1], x * tilesize[0], tilesize[1], tilesize[0])
            tile = pygame.transform.scale(
                image.subsurface(rect), (tilesize[1] * scale, tilesize[0] * scale)
            )
            tile_table.append(tile)

    return tile_table

