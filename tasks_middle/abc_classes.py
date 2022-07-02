from abc import ABC,abstractmethod


# Добавить абстрактный метод 'say()' в класс 'Animal'
class Animal(ABC):
    @abstractmethod
    def say(self):
        pass

class Cat(Animal):
    def say(self):
        print("Mur Mur")

class Dog(Animal):
    def say(self):
        print("Gav Gav")
# Создать два наследника класса Cat & Dog, реализовать абстрактный метод 
# Cat говорит "Мяу"
# Dog говорит "Гав"
c=Cat()
c.say()
d=Dog()
d.say()
# Создать два обьекта кота и собаки и вызвать метод 'say'