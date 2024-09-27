#Given an array of numbers, write a program to check whether
#there are any duplicated elements in the array or not.
#INput
#8
#1 2 3 1 3 6 6 8
#output
#1 3 6 
n=int(input())
l=list(map(int,input().split()))
flag=0
for i in range(0,n):
    for j in range(i+1,n):
        #print(l[i],"->",l[j])
        if(l[i]==l[j]):
            print(l[i],end=" ")
            flag=1
if(flag==0):print("There are no duplicate elements in the array")
