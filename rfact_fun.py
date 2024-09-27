def rfact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*rfact(n-1)

n=int(input("Enter an Integer:"))
print(rfact(n))
