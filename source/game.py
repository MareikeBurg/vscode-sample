import pygame
import os


class Game:
    def __init__(self):
        self.width = 1920
        self.height = 1080
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = []
        self.neutrals = []
        self.units = []
        self.food = 10
        self.wood = 1
        self.stone = 0
        self.copper = 0
        self.steel = 0
        self.mage = 0
        self.background = pygame.image.load(
            os.path.join("assets/sprites", "pinkbackground.png")
        )
        self.clicks = []

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

    def draw(self):
        self.win.blit(self.background, (0, 0))
        for p in self.clicks:
            pygame.draw.circle(self.win, (255, 0, 0), (p[0], p[1]), 5, 0)
        pygame.display.update()


g = Game()
g.run()
