import pygame


class Field:
    def __init__(self, screen):
        self.tiles = [["xxa"], ["xxa"], ["aax"]]
        self.tile_list = create_tile_list()
        self.screen = screen

    def draw(self, x, y):
        self.screen.blit(self.tile_list[0][0], (x, y))


# hardcoded
def create_tile_list():
    tile_width = 32
    tile_height = 32
    image = pygame.image.load("assets/sprites/fantasyhextiles_v3.png").convert()
    tile_table = []
    for tile_x in range(0, 3):
        line = []
        tile_table.append(line)
        for tile_y in range(0, 3):
            rect = (tile_x * tile_width, tile_y * 48 + 18, tile_width, tile_height)
            tile = pygame.transform.scale(
                image.subsurface(rect), (tile_width * 2, tile_height * 2)
            )
            line.append(tile)

    return tile_table

