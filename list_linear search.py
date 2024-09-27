l=list(map(int,input().split()))
b=int(input("Enter an element to be searched in the list:"))
f=0
for i in l:
   if(b==i):
       print("Element is found")
       f=1
       break
if(f==0):
    print("Element is not found")

