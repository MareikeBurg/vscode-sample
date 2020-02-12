import pygame
from field import Field
from unit import Unit
from enemy import Enemy
from projectile import Projectile
import os
import logging
from math import sqrt


class Game:
    """
    main gameloop class
    """

    def __init__(self):
        """
        setup pygame and prepering a new game
        """
        pygame.init()

        try:
            # hardcoded values for diffrent monitor resolutions
            self.width, self.height, self.scale = (
                {1920: 1280, 2560: 1920}[pygame.display.Info().current_w],
                {975: 720, 1335: 1080}[pygame.display.Info().current_h],
                {1920: 2, 2560: 3}[pygame.display.Info().current_w],
            )
        except KeyError:
            # else takes default values
            self.width, self.height, self.scale = 1280, 720, 2
            logging.warning("using default screen resolution")

        # pygame window
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.blit(
            pygame.image.load(os.path.join("assets/sprites", "background.png")), (0, 0)
        )
        # sprites
        self.tile_list = create_sprite_list(self.scale)

        # map
        self.feld = Field(self.window, self.scale, self.tile_list)

        # entities
        self.enemys = []
        self.neutrals = []
        self.projectiles = []

        # ressources
        self.food: int = 10
        self.cost: int = 1
        self.wood: int = 5
        self.stone = 0
        self.year = 0
        self.day = 0

        self.textdraw()
        self.feld.drawall()

        # manual drawings
        # self.feld.draw(500, 500, 41)
        # self.feld.draw(400, 400, 42)
        # self.feld.draw(300, 500, 43)
        self.enemys.append(Enemy(300, 300, self.tile_list[42], self.window, 5, 10, self.scale))
        """
        self.enemys.append(
            Enemy(150, 170, self.feld.getSpritebyNumber(42), self.window, 5, 10, self.scale)
        )"""

        self.projectiles.append(
            Projectile(350, 456, self.tile_list[43], self.window, 1, 10, (300, 300), self.scale)
        )
        """
        self.projectiles.append(
            Projectile(
                450,
                200,
                self.feld.getSpritebyNumber(43),
                self.window,
                1,
                10,
                (150, 170),
                self.scale,
            )
        )"""
        """
        self.enemys.append(
            Enemy(300, 400, self.feld.getSpritebyNumber(42), self.window,30)
        )
        self.enemys.append(
            Enemy(400, 400, self.feld.getSpritebyNumber(42), self.window)
        )"""

    def run(self):
        run = True

        clock = pygame.time.Clock()
        while run:
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pos)

            self.day += 1

            if self.day % 10 == 0:
                self.textdraw()

            if self.day == 1000:
                self.year += 1
                # self.textdraw()

            self.feld.drawall()

            # TODO also update for enemie
            for enemy in self.enemys:
                enemy.update()
                for projectile in self.projectiles:
                    if detectCircularCollision(enemy, projectile):
                        if enemy.hit(projectile):
                            self.enemys.remove(enemy)
                        self.projectiles.remove(projectile)

            for projectile in self.projectiles:
                projectile.update()

            pygame.display.update()

        pygame.quit()

    def textdraw(self):
        """
        draws the ressource bar at the top
        """
        self.window.blit(
            pygame.image.load(os.path.join("assets/sprites", "background.png")), (0, 0)
        )
        myfont = pygame.font.SysFont("monospace", 10 * self.scale)
        text = myfont.render("Food: " + str(self.food), 1, (0, 0, 0))
        self.window.blit(text, (50, 50))
        text = myfont.render("- " + str(self.cost), 1, (255, 0, 0))
        self.window.blit(text, (50 + 75 * self.scale, 50))
        text = myfont.render("Wood: " + str(self.wood), 1, (0, 0, 0))
        self.window.blit(text, (50 + 200 * self.scale, 50))
        text = myfont.render("Stone: " + str(self.stone), 1, (0, 0, 0))
        self.window.blit(text, (50 + 300 * self.scale, 50))
        text = myfont.render("Year: " + str(self.year), 1, (0, 0, 0))
        self.window.blit(text, (50 + 400 * self.scale, 50))

        self.window.blit(
            myfont.render("Day: " + str(self.day), 1, (0, 0, 0)), (50 + 500 * self.scale, 50)
        )

    def clicked(self, pos):
        """
        activated on clicking inside the game, triggers actions depending on clicked location
        
        Arguments:
            pos {(int,int)} -- position in which the click occured
        """


def detectCircularCollision(uni1: Unit, uni2: Unit):
    """
    checks if the two units are in each others collison range, based on
    https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection
    
    Arguments:
        uni1 {Unit} -- first unit, for example an enemey
        uni2 {Unit} -- second unit, for example an projectile
    
    Returns:
        bool -- true if the units collide, else false
    """

    # sprites are top left corner centered -> offset
    dx = uni1.x + uni1.centerxoffset - uni2.x + uni2.centerxoffset
    dy = uni1.y + uni1.centeryoffset - uni2.y + uni2.centeryoffset
    print("uni1: ", uni1.x, uni1.y)
    print("uni2: ", uni2.x, uni2.y)
    print(sqrt(dx * dx + dy * dy), uni1.collisonradius + uni2.collisonradius)

    if sqrt(dx * dx + dy * dy) < uni1.collisonradius + uni2.collisonradius:
        logging.debug(
            "collision detected at "
            + str(uni1.x)
            + " "
            + str(uni1.y)
            + " , "
            + str(uni1)
            + " and "
            + str(uni2)
        )
        return True

    return False


# hardcoded
def create_sprite_list(scale):
    """
    one tile is 48 pixel high and 32 pixels wide, the spriteset is 6 tiles high and 8 tiles wides. 
    Height total 48*6=288, width total 32*8=256

    returns a list of all sprites
    """
    tilesize = (48, 32)
    spritesize = (288, 256)
    spritelocation = "assets/sprites/fantasyhextiles_v3.png"

    image = pygame.image.load(spritelocation).convert_alpha()
    tile_table = []
    for x in range(0, int(spritesize[0] / tilesize[0])):
        for y in range(0, int(spritesize[1] / tilesize[1])):

            rect = (y * tilesize[1], x * tilesize[0], tilesize[1], tilesize[0])

            tile = pygame.transform.scale(
                image.subsurface(rect), (tilesize[1] * scale, tilesize[0] * scale)
            )
            tile_table.append(tile)
    return tile_table
