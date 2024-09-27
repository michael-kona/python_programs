n=int(input())
s=0
m=n
while m!=0:
   r=m%10
   s=s+r**3
   m=m//10
if s==n:print("armstrong")
else: print("not an armstrong")
