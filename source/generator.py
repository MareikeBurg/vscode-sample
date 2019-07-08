import random


class Generator:
    """
    Generates diffrent kinds of terrain
    """

    def __init__(self):
        self.seed = 1

    # TODO allowedTiles aktiviweren
    def random(self, width: int, height: int, allowedTiles: [int]):
        """
        [Generates all tiles random from the list of allowedTIles]
        
        Arguments:
            width {int} -- number of tiles in x direction
            height {int} -- number of tiles in y direction
            allowedTiles {[int]} -- list of tiles which can occure in the generated tiles
        
        Returns:
            [int][int] -- double array of tiles
        """

        layout = [[0 for x in range(height)] for y in range(width)]

        for i in range(height):
            for j in range(width):
                # rand = random.randint(0, 10)
                layout[i][j] = random.randint(0, 6)
        return layout

    def custom(self, width: int, height: int, allowedTiles: [int]):
        """
        template for future custom worldgen
        
        Arguments:
            width {int} -- [description]
            height {int} -- [description]
            allowedTiles {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """

        layout = [[0 for x in range(height)] for y in range(width)]

        for i in range(5):
            # rand = random.randint(0, 10)
            layout[random.randint(0, width - 1)][random.randint(0, height - 1)] = 6

        for i in range(5):
            # rand = random.randint(0, 10)
            layout[random.randint(0, width - 1)][random.randint(0, height - 1)] = 2

        for i in range(5):
            # rand = random.randint(0, 10)
            layout[random.randint(0, width - 1)][random.randint(0, height - 1)] = 1
        return layout

