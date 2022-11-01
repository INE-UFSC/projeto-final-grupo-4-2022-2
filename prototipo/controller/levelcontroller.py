from utility.constants import STATE_END_GAME, ASTEROID_TAG, VELOCITY_MULTIPLIER, TIME_TO_SCORE
from controller.gamecontroller import GameController
from model.entities.player import Player
from controller.entitiescontroller import EntitiesController


# Sugestão para import das constantes
# , OUTRA_CONSTANTE, ULTIMA_CONSTANTE


class LevelController:

    def __init__(self, player: Player = None) -> None:
        self.__player = player
        self.__last_update = 0

    def set_player(self, player: Player):
        self.__player = player

    def get_player(self) -> Player:
        return self.__player

    def update(self) -> None:
        if not self.get_player().alive():
            next_state = STATE_END_GAME
            GameController.instance().change_state(next_state)

    def increase_speed(self):
        for i in EntitiesController.instance().get_entities():
            if i.get_tag() == ASTEROID_TAG:
                body = i.get_body()
                new_velocity = body.get_velocity() * VELOCITY_MULTIPLIER
                body.set_velocity(new_velocity)

    def countdown(self, dt: float):
        self.__last_update += dt
        if self.__last_update > TIME_TO_SCORE:
            self.__last_update = 0
            self.increase_speed()
