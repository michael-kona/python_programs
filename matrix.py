r=int(input())
c=int(input())
mat=[]
for i in range(r):
    #row=[]
    row=list(map(int,input().split()))
    mat.append(row)
for i in range(r):
    for j in range(c):
        print(mat[i][j],end=" ")
    print(sum(mat[i]))
    print("")

