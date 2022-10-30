
from utility.data.DAO import DAO
from utility.data.scorelog import ScoreLog


class ScoreDAO(DAO):
    def __init__(self) -> None:
        super().__init__('scores.pkl')

    def add(self, score: ScoreLog):
        old_score = self.get(score.get_name())
        if old_score is None:
            super().add(score.get_name(), score)
        elif old_score.get_score() < score.get_score():
            super().add(score.get_name(), score)