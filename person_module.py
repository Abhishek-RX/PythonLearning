class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}."

    def is_adult(self):
        return self.age >= 18

    def celebrate_birthday(self):
        self.age += 1
        return f"Happy Birthday {self.name}! You are now {self.age} years old."
