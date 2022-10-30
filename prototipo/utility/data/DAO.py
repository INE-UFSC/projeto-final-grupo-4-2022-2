from abc import ABC
import pickle


class DAO(ABC):
    def __init__(self, datasource='') -> None:
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def get(self, key):
        return self.__cache.get(key)

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError as e:
            print(e)

    def get_all(self):
        return self.__cache.values()
