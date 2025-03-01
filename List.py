lst = list() 
for i in range (10):
    lst.append(i)
lst.extend([10,11,12,13])
lst.pop()
lst.reverse()
lst.reverse() 
lst.remove(0)
print(lst) 

flag = False
k = 12 
for i in range(len(lst)):
    if(lst[i] == k):
        print("Element found ",i)
        flag = True
        break 
if(flag == False):
    print("Element not found")
    
    

# TWO Sum Problem 

pairSum = 22 
p1 = 0 
p2 =len(lst)-1 

while(p1<p2):
    if(lst[p1] + lst[p2] == pairSum):
        print(" pair found at indexs", p1,p2 )
        break 
    elif(lst[p1] + lst[p2] > pairSum):
        p2 = p2-1 
    else :
        p1+=1 
        
if(p1>=p2):
    print("Pair not found")
        
# List comprehension (Short way to create list)*******************************

lst = [ x**2 for x in range(10) if x%2 == 0] 
print(lst)       

EvenOdd = ["Even" if x%2 ==0 else "Odd" for x in range(1,10)]
print(EvenOdd)

