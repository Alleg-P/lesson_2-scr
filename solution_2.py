# Задание 2: Работа с атрибутами класса

class Person:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2022 - birth_year
        return cls(name, age)

    @classmethod
    def get_population(cls):
        print("Current population:", cls.population)

person1 = Person("Alice", 25)
person2 = Person.from_birth_year("Bob", 1990)
Person.get_population()
