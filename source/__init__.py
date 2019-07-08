import logging
from game import Game

# logging options: DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)

g = Game()
g.run()
