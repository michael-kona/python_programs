l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s=0
if (len(l1)==len(l2)):
   for i in range(len(l1)):
      s=s+(l1[i]*l2[i])
   print("DOT PRODUCT:",s)
else:
   print("DOT PRODUCT is not possible")

