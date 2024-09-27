s=input()
l=list(s)
n=len(s)
i=0
j=n-1
while i<j:
    if l[i].isalpha() and l[j].isalpha():
        t=l[i]
        l[i]=l[j]
        l[j]=t
        i=i+1
        j=j-1
    elif not l[i].isalpha():
        i=i+1
    else:
        j=j-1
print("".join(l))
