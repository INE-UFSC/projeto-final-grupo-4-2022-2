from abc import ABC
import pickle


# Classe para persistência
class DAO(ABC):

    def __init__(self, datasource='') -> None:
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    # Persiste os dados em disco
    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    # Resgata os dados em disco
    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    # Adiciona novos dados em cache
    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    # Resgata algum dado específico do cache
    def get(self, key):
        return self.__cache.get(key)

    # Remove algum dado específico do cache
    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError as e:
            print(e)

    # Resgata todos os dados do cache
    def get_all(self):
        return self.__cache.values()
