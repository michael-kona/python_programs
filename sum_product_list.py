n=input()
l=list(input().split())
f=0
if(n.strip().isnumeric()):
    n=int(n)
    sum=0
    prod=1
    for i in range(n):
        if(not l[i].isalpha()):
            sum=sum+int(l[i])
            prod=prod*int(l[i])
        else:
            f=1
            print("Invalid")
            break
else:
    f=1
    print("Invalid")
    
if(f==0):
        print("sum:",sum)
        print("Product:",prod)
