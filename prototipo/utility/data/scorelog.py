
class ScoreLog():

    def __init__(self, score: int, nome: str):
        self.__score = score
        self.__nome = nome

    def get_score(self):
        return self.__score

    def get_nome(self):
        return self.__nome

    def __str__(self):
        return f"Nome: {self.__nome}, Score: {self.__score}"
