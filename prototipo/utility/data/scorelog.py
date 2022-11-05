

# Classe para armazenar as informações do score
class ScoreLog():

    def __init__(self, score: int, name: str):
        self.__score = score
        self.__name = name

    def get_score(self):
        return self.__score

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Name: {self.__name}, Score: {self.__score}"
