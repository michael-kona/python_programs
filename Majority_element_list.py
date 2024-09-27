n=int(input())
l=list(map(int,input().split()))
f=0
for i in range(n-1):
    c=0
    for j in range(i+1,n):
        if l[i]==l[j]:
            c=c+1
    
    if c>=n//2:
        f=1
        print(l[i])
        break
if f==0: print(0)
