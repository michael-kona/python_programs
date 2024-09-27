l=list(map(int,input().split()))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if(l[i]>l[j]):
            t=l[i]
            l[i]=l[j]
            l[j]=t
print(l)
