def demo():
    print("hello! I am a function demo")
    #return "END"
    
print(demo())
print("I am outside the function")


def add(a,b):
    print("Sum of a and b ")
    return a + b

Result = add(10,42)
print(Result)

def Average_of_LIST(lst):
    sum = 0
    for i in lst:
        sum += i
        
    average = sum / len(lst)
    return round(average,3)  # Limiting to 2 decimal placesreturn f"{average:.2f}"  # Limiting to 2 decimal places
    
    
LST = [2,5,6,525,8,90,754,5,442,3,2,1] 
print(type(LST))   
AVG = Average_of_LIST(LST)  # Output: 153.67
print(AVG)  # Output: 153.67


def EmptyFunction():
    pass
