# Abstract Base Copy
# ABC menas abstract class whihc restrict other class
from abc import ABC, abstractmethod


class Animal(ABC):   # abstract class
    def eat(self):
        print("Eating")

    @abstractmethod
    def die(self):
        pass


class Bird(Animal):
    def fly(self):
        print("Flying")

    def die():  # as Animal is a abstract class inherited so the method needs to be created
        print("Died")


class Fish(Animal):
    def swim(self):
        print("Swimming")


Bird = Bird()
print(Bird)
