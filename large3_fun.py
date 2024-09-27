def max(a,b,c):
    if(a>b and a>c):
        return(a)
    elif(b>c):
        return(b)
    else:
        return(c)

a,b,c=input().split(",")
print("largest no. is",max(a,b,c))
