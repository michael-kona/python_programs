n=int(input())
test=[]
weight=[]
for i in range(n):
    a,b=input().split()
    test.append(int(a))
    weight.append(float(b))
#print(test)
#print(weight)
sum1=0
sum2=0
for i in range(n):
    sum1=sum1+(test[i]*weight[i])
    sum2=sum2+weight[i]
ans=sum1/sum2
print("%.2f"%ans )
