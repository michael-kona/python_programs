l=list(map(int,input().split()))
b=int(input("Enter an element to be searched in the list:"))
f=0
low=0
high=len(l)-1
while low<high:
    mid=(low+high)//2
    if(b==l[mid]):
        print("Element found at position",mid+1)
        f=1
        break
    elif(b<l[mid]):
        high=mid-1
    else:
        low=mid+1
if(f==0):print("Element is not found")
