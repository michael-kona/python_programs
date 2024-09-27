n=int(input())
l=list(map(int,input().split()))
if n>0 and n<=10:
    max=-1
    min=999
    for i in range(n):
        if l[i]>max:
            max=l[i]
        if l[i]<min:
            min=l[i]
    print("Max:",max)
    print("Min:",min)
else:
    print("Invalid")
