r=int(input("Enter row count:"))
c=int(input("Enter Col count:"))
mat=[]
for i in range(r):
    row=list(map(int,input().split()))
    mat.append(row)
for i in range(r):
    for j in range(c):
        print(mat[i][j],end=" ")
    print(sum(mat[i]))
