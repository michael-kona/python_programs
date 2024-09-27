n=int(input())
l=list(map(int,input().split()))
t=l[0]
for i in range(n-1):
    l[i]=l[i+1]
l[i+1]=t
for i in range(n):
    print(l[i],end=" ")
