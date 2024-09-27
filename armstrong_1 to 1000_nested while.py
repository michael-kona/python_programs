i=1
while i<=1000:
    s=0
    m=i
    while m!=0:
        r=m%10
        s=s+r**3
        m=m//10
    if(s==i):
        print(i)
    i=i+1
