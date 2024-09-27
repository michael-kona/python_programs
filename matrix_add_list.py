r=int(input("Enter no. of rows:"))
c=int(input("Enter no. of cols:"))
print("Enter first matrix(one row in one line):")
m1=[]
for i in range(r):
    l=list(map(int,input().split()))
    m1.append(l)
print("Enter second matrix(one row in one line):")
m2=[]
for i in range(r):
    l=list(map(int,input().split()))
    m2.append(l)
m3=[]
for i in range(r):
    l=[]
    for j in range(c):
        l.append(0)
    m3.append(l)
print("Resultant matrix:") 
for i in range(r):
    for j in range(c):
        m3[i][j]=m1[i][j]+m2[i][j]
        print(m3[i][j],end=" ")
    print("")

