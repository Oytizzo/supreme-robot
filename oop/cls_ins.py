# Python oop checking

class Person:
    def __init__(self, first, last, email) -> None:
        # This is initializer or constructor
        self.first = first
        self.last = last
        self.email = email


person_1 = Person("Mike", "Tyson", "mike@boxer.com")
person_2 = Person("Neil", "Tyson", "neil@nasa.com")

print(person_1.email)
print(person_2.email)
