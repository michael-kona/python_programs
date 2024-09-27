n=int(input())
l=list(map(int,input().split()))    
count=0
for i in range(n-1):
    f=0
    for j in range(i+1,n):
        if l[i]<l[j]:
            f=1
            break
    if f==0: count=count+1
print(count+1)
