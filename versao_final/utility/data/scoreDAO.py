
from utility.data.DAO import DAO
from utility.data.score import Score

# DAO para o score


class ScoreDAO(DAO):

    def __init__(self) -> None:
        super().__init__('scores.pkl')

    def add(self, score: Score) -> None:
        # Adiciona um novo score caso não exista um ou
        # caso seja maior que o antigo
        old_score = self.get(score.get_name())
        if old_score is None:
            super().add(score.get_name(), score)
        elif old_score.get_points() < score.get_points():
            super().add(score.get_name(), score)
