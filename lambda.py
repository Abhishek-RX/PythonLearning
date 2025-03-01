# Lambda 

add = lambda x, y : x+y 

print(add(1, 2))
print(add("A", "B"))

Square = lambda x : x**2 
print(Square(25))

div = lambda x, y : x/y if y!= 0 else "Division by zero is not allowed."
print(div(2,0))

lst = [1, 2, 3, 4, 5] 
square = list(map(lambda x : x**2,lst))
print(square)

even = list(filter(lambda x :  x%2 == 0, lst ))
print(even)

# Reduce function 
from functools import reduce

Sum = reduce(lambda x, y : x+y , lst )
print(Sum)