# Methods in Python

from person_module import Person

# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Calling methods
print(person1.greet())  # Output: Hello, my name is Alice.
print(f"Is {person1.name} an adult? {'Yes' if person1.is_adult() else 'No'}")  # Output: Yes

# Demonstrating the new method
print(person1.celebrate_birthday())  # Output: Happy Birthday Alice! You are now 31 years old.
