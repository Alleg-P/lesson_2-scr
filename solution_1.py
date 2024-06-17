# Задание 1: Альтернативные конструкторы

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2022
        age = current_year - birth_year
        return cls(name, age)

person = Person.from_birth_year("Alice", 1990)

print(f"Имя: {person.name}")
print(f"Возраст: {person.age}")
