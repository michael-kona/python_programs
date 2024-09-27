n=int(input())
i=2
f=0
while i<=n/2:
       if n%i==0:
           f=1
           break
       i=i+1
if f==0:print("Prime")
else:print("Not a Prime")
