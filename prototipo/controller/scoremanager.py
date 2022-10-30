

from controller.entitiescontroller import EntitiesController
from utility.data.scoreDAO import ScoreDAO
from utility.data.scorelog import ScoreLog
import utility.constants as CONSTANTE


class ScoreManager:

    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.__score = 0
        self.__score_dao = ScoreDAO()
        self.last_update = 0

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        self.__score = new_score

    def get_score_dao(self):
        return self.__score_dao

    def reset_score(self):
        self.__score = 0

    def increase(self, value):
        self.set_score(self.get_score() + value)

    def update_score(self, dt: float):
        self.last_update += dt
        if self.last_update > CONSTANTE.TIME_TO_SCORE:
            self.last_update = 0
            self.increase(CONSTANTE.TIME_SCORE)
        for entitie in EntitiesController.instance().get_deletion_buffer():
            if entitie.get_tag() == CONSTANTE.ASTEROID_TAG:
                self.increase(CONSTANTE.DESTROY_SCORE)
            if entitie.get_tag() == CONSTANTE.ALIEN_TAG:
                self.increase(CONSTANTE.DESTROY_SCORE)

    def generate_score_log(self, name, score) -> ScoreLog:
        print(ScoreLog(score, name))
        return ScoreLog(score, name)
    
    def write_to_disk(self, score_log: ScoreLog) -> bool:
        self.get_score_dao().add(score_log)
