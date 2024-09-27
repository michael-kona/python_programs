n=int(input())
l=list(map(int,input().split()))
item=int(input())
index=int(input())

l.append(0)

for i in range(n,index,-1):
    l[i]=l[i-1]
l[index]=item
print(l)
