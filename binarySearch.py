k = 25
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

n= len(lst)
low = 0 
high = n-1 
count = 0
flag = False
while(low<=high):
     mid = low + (high - low ) // 2 
     
     if lst[mid]==k :
        print("element found at index ", mid)
        flag = True 
        break
     elif lst[mid] > k :
        high = mid-1 
     else:
        low  = mid+1 
     count+=1     

print("Number of iterations ", count)      
if(flag == False):
    print("Element not found")
