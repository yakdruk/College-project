from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def get_details(self):
        pass
