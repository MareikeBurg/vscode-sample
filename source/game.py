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

        # pygame window
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.blit(
            pygame.image.load(os.path.join("assets/sprites", "background.png")), (0, 0)
        )

        # map
        self.feld = Field(self.window, self.scale)

        # entities
        self.enemys = []
        self.neutrals = []
        self.units = []

        # ressources
        self.food: int = 10
        self.cost: int = 1
        self.wood: int = 5
        self.stone = 0

        self.textdraw()
        self.feld.drawall()

        # manual drawings
        self.feld.draw(500, 500, 41)
        self.feld.draw(400, 400, 42)
        self.feld.draw(300, 500, 43)

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
                    print(pos)

            pygame.display.update()

        pygame.quit()

    def textdraw(self):
        """
        draws the ressource bar at the top
        """

        myfont = pygame.font.SysFont("monospace", 10 * self.scale)
        text = myfont.render("Food: " + str(self.food), 1, (0, 0, 0))
        self.window.blit(text, (50, 50))
        text = myfont.render("- " + str(self.cost), 1, (255, 0, 0))
        self.window.blit(text, (50 + 75 * self.scale, 50))
        text = myfont.render("Wood: " + str(self.wood), 1, (0, 0, 0))
        self.window.blit(text, (50 + 200 * self.scale, 50))
        text = myfont.render("Stone: " + str(self.stone), 1, (0, 0, 0))
        self.window.blit(text, (50 + 300 * self.scale, 50))

    def clicked(self, pos):
        """
        activated on clicking inside the game, triggers actions depending on clicked location
        
        Arguments:
            pos {(int,int)} -- position in which the click occured
        """

