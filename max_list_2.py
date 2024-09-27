l=list(map(int,input().split()))
max=l[0]
for i in l:
    if max<i:
        max=i
print("Largest element is:",max)
