
from utility.data.DAO import DAO
from utility.data.scorelog import ScoreLog


class ScoreDAO(DAO):
    def __init__(self) -> None:
        super().__init__('scores.pkl')

    def add(self, score: ScoreLog):
        if (score is not None) and (isinstance(score.get_score(), int)) and isinstance(score, ScoreLog):
            id = self.get_last_id()
            super().add(id, score)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

    def get_last_id(self):
        carregar = super().load()
        if carregar is None:
            return -1
        return list(carregar.keys())[-1]
