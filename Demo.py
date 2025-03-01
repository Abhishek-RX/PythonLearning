print("Hello world!")

first_num = 5
second_num = 10
print(first_num + second_num)
print(type(first_num))

# print((first_num**second_num)**second_num)

s = "Abhishek"
print(s[2])
print(s[2:])
print(s[:5])
print(s[2:5])
print(s[-1])

arry = [1, 2, 3, 4, 5]
print(arry[2])

arry.append(6)
print(arry)

for i in range(len(arry)):
    if i == len(arry) - 1:
        print(arry[i], end="")
    else:
        print(arry[i], end=" , ")

print("\nhello")

arry.insert(2, 10)
print(arry)

arry.remove(1)
print("After REMOVE: ", arry)

arry.pop(2)
print("After POP ", arry)

a = 1000
b = 20
c = 100

if(a>b and a>c ):
    print("A is greater")
elif(b>c and b > a ):
    print("B is greater")
else :
    print("C is greater")
    
j=1  
while( j <=10):
    print("5 X ",j, " = ",5*j)
    j+=1 
    
String = "Abhsihek"