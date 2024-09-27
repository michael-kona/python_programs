def rfib(n):
    if(n==1):
        return 0
    elif (n==2):
        return 1
    else:
        return rfib(n-1)+rfib(n-2)

n=int(input("Enter an Integer:"))
print(rfib(n))
