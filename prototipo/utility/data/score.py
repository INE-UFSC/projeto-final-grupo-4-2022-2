

# Classe para armazenar as informações do score
class Score:

    def __init__(self, points: int, name: str):
        self.__points = points
        self.__name = name

    def get_points(self):
        return self.__points

    def set_points(self, new_points):
        self.__points = new_points

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def increase(self, value):
        self.__points += value

    def __str__(self):
        return f"Name: {self.__name}, Score: {self.__points}"
