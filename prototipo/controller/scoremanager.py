
from utility.data.scoreDAO import ScoreDAO
from utility.constants.score_constants import ScoreConstants
from utility.constants.asteroid_constants import AsteroidConstants
from utility.constants.alien_constants import AlienConstants
from model.entities.player import Player

# Singleton para gerenciar o score do player


class ScoreManager:

    def __init__(self, player: Player = None) -> None:
        self.__player = player
        self.__score_dao = ScoreDAO()
        self.last_update = 0

    def update_score(self, dt: float, deletion_buffer: list) -> None:
        self.last_update += dt

        if self.__player is None:
            return

        if not isinstance(self.__player, Player):
            return

        # Incrementa o score ao longo do tempo e com a destruição de entidades
        if self.last_update > ScoreConstants().time_to_score:
            self.last_update = 0
            self.__player.get_score().increase(ScoreConstants().time)
        for entity in deletion_buffer:
            if entity.get_tag() == AsteroidConstants().tag:
                self.__player.get_score().increase(ScoreConstants().destroy)
            elif entity.get_tag() == AlienConstants().tag:
                self.__player.get_score().increase(ScoreConstants().destroy)

    def write_to_disk(self, new_name: str) -> None:
        if self.__player is None:
            return

        # Atualiza o nome do jogador e escreve em disco
        self.__player.get_score().set_name(new_name)
        self.__score_dao.add(self.__player.get_score())
