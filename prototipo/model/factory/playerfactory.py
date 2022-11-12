
from model.entities.player import Player
from model.body import Body

from utility.constants.game_constants import GameConstants
from utility.constants.player_constants import PlayerConstants

from math import ceil
from pygame.math import Vector2


class PlayerFactory:

    def create(self) -> Player:
        player_body = Body(Vector2(ceil(GameConstants().screen_size.x/2),
                           ceil(GameConstants().screen_size.y/2)),
                           Vector2(0, 0), PlayerConstants().size)
        player_lives = PlayerConstants().max_lives
        player = Player(player_body, player_lives)
        return player
