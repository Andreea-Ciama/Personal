from domain import Situation

from validators import GameValidator
from service import GameController

from UI import Console

situation = Situation()
game_validator = GameValidator()

game_controller = GameController(situation, game_validator)

console = Console(game_controller)

console.start_game()