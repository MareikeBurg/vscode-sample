import pygame
from field import Field
import os
import logging


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

        self.window = pygame.display.set_mode((self.width, self.height))
        self.enemys = []
        self.neutrals = []
        self.units = []
        self.food: int = 10
        self.wood: int = 1
        self.stone = 0
        self.copper = 0
        self.steel = 0
        self.mage = 0
        self.background = pygame.image.load(
            os.path.join("assets/sprites", "pinkbackground.png")
        )
        self.clicks = []
        self.feld = Field(self.window, self.scale)

    def run(self):
        run = True

        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    print(pos)

            self.draw()

        pygame.quit()

    def clicked(self, pos):
        """
        activated on clicking inside the game, triggers actions depending on clicked location
        
        Arguments:
            pos {(int,int)} -- position in which the click occured
        """

    def draw(self):
        # self.win.blit(self.background, (0, 0))
        # for p in self.clicks:
        # pygame.draw.circle(self.win, (255, 0, 0), (p[0], p[1]), 5, 0)

        self.feld.drawall()
        # pygame.display.flip()
        """
        self.feld.draw(100, 100, "grass")
        self.feld.draw(100, 100 + 1 * 32, "forest")
        self.feld.draw(100 + 24, 100 + 16, "water")
        self.feld.draw(100 + 24, 100 + 16 + 32, "mount")
        self.feld.draw(200, 200, "mount")
        self.feld.draw(200, 200 + 1 * 32, "water")
        """
        pygame.display.update()

