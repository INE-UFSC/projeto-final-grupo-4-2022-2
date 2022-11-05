
from utility.data.DAO import DAO
from utility.data.scorelog import ScoreLog

# DAO para o score
class ScoreDAO(DAO):

    def __init__(self) -> None:
        super().__init__('scores.pkl')

    def add(self, score: ScoreLog):
        # Adiciona um novo score caso não exista um ou
        # caso seja maior que o antigo
        old_score = self.get(score.get_name())
        if old_score is None:
            super().add(score.get_name(), score)
        elif old_score.get_score() < score.get_score():
            super().add(score.get_name(), score)