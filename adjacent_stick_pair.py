n=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(0,n,2):
    if (i==n-1 and n%2==1):
        sum=sum+l[i]
        break
    if (l[i]<l[i+1]):
        sum=sum+l[i]
    else:
        sum=sum+l[i+1]
print(sum)
        
