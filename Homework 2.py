# Розширте клас "Person" з попереднього завдання, додавши методи для зміни значень імені та віку.
# Зробіть так, щоб ім'я не могло містити цифр, а вік був обмежений в діапазоні від 0 до 120.
# При спробі встановити недійсне значення, виведіть повідомлення про помилку.
# (приклад у презентації)
import re


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
            return self.__name

    def get_age(self):
        return self.__age

    import re

    def set_name(self, name):
        if re.match(r"^\D+$", name):
            self.__name = name
            return self.__name
        else:
            return False

    def set_age(self, age):
        if age in range(120):
            self.__age = age
            return age
        else:
            return False



person = Person("Mike25", 305)

print(person.set_name("Mike"))
print(person.set_age(20))

print(person.set_name("Mik3e"))
print(person.set_age(250))
