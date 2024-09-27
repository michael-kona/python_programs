s=input()
n=len(s)
l=list(s)
for i in range(n):
    for j in range(i+1,n):
        if l[i]>l[j]:
            t=l[i]
            l[i]=l[j]
            l[j]=t
str=""
print(str.join(l))
            
