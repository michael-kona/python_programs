n=int(input())
f=0
s=1
if(n<=0):print("Invalid input")
elif(n==1):print(f)
elif(n>=2):
        print(f,s,end=' ',sep=' ')
        for i in range(3,n,1):
            t=f+s
            f=s
            s=t
            print(t,end=' ',sep=' ')
