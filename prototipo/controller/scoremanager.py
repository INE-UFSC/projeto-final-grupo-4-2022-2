

from controller.entitiescontroller import EntitiesController
import utility.constants as CONSTANT


class ScoreManager:

    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.__score = 0
        self.last_update = 0

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        self.__score = new_score

    def reset_score(self):
        self.__score = 0

    def increase(self, value):
        self.set_score(self.get_score() + value)

    def update_score(self, dt: float):
        self.last_update += dt
        if self.last_update > CONSTANT.TIME_TO_SCORE:
            self.last_update = 0
            self.increase(CONSTANT.TIME_SCORE)
        for entitie in EntitiesController.instance().get_deletion_buffer():
            if entitie.get_tag() == CONSTANT.ASTEROID_TAG:
                self.increase(CONSTANT.DESTROY_SCORE)
