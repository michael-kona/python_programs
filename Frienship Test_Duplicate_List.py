n=int(input())
l=list(map(int,input().split()))
for i in range(n-1):
    for j in range(i+1,n):
        if l[i]==l[j]:
            l[j]=-1
c=0
for i in range(n):
    if l[i]!=-1:
        c=c+1
print(c)
