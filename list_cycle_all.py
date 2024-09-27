#Write a program that will cycle all elements of an array
#from one position to the left.
#Input:
#8
#-1 2 -4 3 7 6 102 41
#Output:
#2 -4 3 7 6 102 41 -1
n=int(input())
l=list(map(int,input().split()))
i=0
t=l[0]
while i<n-1:
    l[i]=l[i+1]
    i=i+1
l[i]=t
print(l)
