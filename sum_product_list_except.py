try:
    n=int(input())
    l=list(map(int,input().split()))
    if n<0:
        print("InValid")
    else:
        s=0
        p=1
        for i in range(n):
           s=s+l[i] 
           p=p*l[i]
        print("Sum:",s,sep="")
        print("product:",p,sep="")
except ValueError:
    print("Invalid")
