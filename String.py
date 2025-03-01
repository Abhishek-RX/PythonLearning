Str = "Racecar"
String = Str.upper()
revString = ""
for i in range(len(String)):
    revString = String[i]+revString 
print(revString)
    
if(String == revString):
    print("Palindrome")
else:
    print("Not a Palindrome")    
    
    
    
