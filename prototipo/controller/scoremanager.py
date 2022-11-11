
from utility.data.scoreDAO import ScoreDAO
import utility.constants as CONSTANT


# Singleton para gerenciar o score do player
class ScoreManager:

    def __init__(self, player):
        self.__player = player
        self.__score_dao = ScoreDAO()
        self.last_update = 0

    def get_dao(self):
        return self.__score_dao

    def update_score(self, dt: float, deletion_buffer):
        self.last_update += dt
        if self.last_update > CONSTANT.TIME_TO_SCORE:
            self.last_update = 0
            self.__player.get_score().increase(CONSTANT.TIME_SCORE)
        for entity in deletion_buffer:
            if entity.get_tag() == CONSTANT.ASTEROID_TAG:
                self.__player.get_score().increase(CONSTANT.DESTROY_SCORE)
            elif entity.get_tag() == CONSTANT.ALIEN_TAG:
                self.__player.get_score().increase(CONSTANT.DESTROY_SCORE)

    def write_to_disk(self, new_name) -> bool:
        self.__player.get_score().set_name(new_name)
        self.__score_dao.add(self.__player.get_score())
