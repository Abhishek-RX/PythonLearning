import random

# Generate a random integer between 1 and 10
random_int = random.randint(1, 10)
print(f"Random integer between 1 and 10: {random_int}")

# Generate a random float between 0.0 and 1.0
random_float = random.random()
print(f"Random float between 0.0 and 1.0: {random_float}")

# Generate a random float between 1.0 and 10.0
random_uniform = random.uniform(1.0, 10.0)
print(f"Random float between 1.0 and 10.0: {random_uniform}")

# Choose a random element from a list
elements = ['apple', 'banana', 'cherry', 'date']
random_choice = random.choice(elements)
print(f"Random choice from list: {random_choice}")

# Generate a list of 3 unique random elements from a list
random_sample = random.sample(elements, 3)
print(f"Random sample of 3 elements from list: {random_sample}")
