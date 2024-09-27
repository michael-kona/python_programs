l=list(map(int,input().split()))
n=len(l)
for i in range(n):
    for j in range(i+1,n):
        if l[i]>l[j]:
            t=l[i]
            l[i]=l[j]
            l[j]=t
print(l)
            
