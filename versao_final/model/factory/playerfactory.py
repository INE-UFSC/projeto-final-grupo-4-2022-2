
from abc import ABC

from model.entities.player import Player
from model.body import Body

from utility.constants.player_constants import PlayerConstants

from pygame.math import Vector2


class PlayerFactory(ABC):

    def create(self) -> Player:
        player_body = Body(Vector2(0, 0),
                           Vector2(0, 0), PlayerConstants().size)
        player_lives = PlayerConstants().max_lives
        player = Player(player_body, player_lives)
        player.reset()
        return player
