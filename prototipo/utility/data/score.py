
class Score:
    ...
# Classe para armazenar as informações do score


class Score:

    def __init__(self, points: int, name: str):
        self.__points = points
        self.__name = name

    def get_points(self) -> int:
        return self.__points

    def set_points(self, new_points: int) -> None:
        self.__points = new_points

    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name: str) -> None:
        self.__name = new_name

    def increase(self, value: int) -> None:
        self.__points += value

    def __str__(self):
        return f"{self.__name} = {self.__points}"

    def __lt__(self, other: Score) -> bool:
        if self.get_points() < other.get_points():
            return True

        return False
