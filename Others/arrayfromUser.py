from array import *

arr = array('i',[])
n= int(input("Enter the array length"))
for i in range(n):
    #arr.append(int(input("enter value"))) or
    x=int(input("enter value"))
    arr.append(x)
for i in arr : 
    print(i)


n= int(input("Enter the number to find index"))
k=0
for element in arr:
    if element==n :
        print(k)
        break
    k+=1
else : print("not found")

#if you use inbuilt function instead of above code from K=0

print("index no: ",arr.index(n))
