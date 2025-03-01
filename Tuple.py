# Tuple 
# Tuple is a collection of immutable Python objects. 
# The tuples cannot be changed unlike lists and dictionaries. 
# Tuples use parentheses, whereas lists use square brackets.
# Here is an example of a tuple:  tuple = (123, 'hello').   
# Tuples are faster than lists, but they cannot be changed.
# Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing.
# Tuples can be used as keys in dictionaries, while lists cannot.

Tuple = ("Hello", "World",80085, 3.14, 1,2,3,4,5,4,7,8,5,1) 

print(Tuple[-1]) # Accessing the last element of the tuple;
print(Tuple[1:3]) # Accessing elements from index 1 to 2;                                  
print(Tuple.count(4)) # Counting the number of times 4 appears in the tuple;
print(Tuple.index(5)) # Finding the index of the first occurrence of 5 in the tuple;

a,b,c = Tuple[:3] # Unpacking the first three elements of the tuple;
print(a,b,c)

inputElement =input("Enter the element")
new_Tuple = Tuple + (inputElement,) # Adding a new element to the tuple;
print(new_Tuple)