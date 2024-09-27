n=int(input())
f=2
s=3
i=3
#print(f,s,sep=" ",end=" ")
while(True):
    t=f+s
    #print(t,end=" ")
    j=s+1
    while(j<t):
        print(j,sep=" ",end=" ")
        j=j+1
        if(j>n):break;
    if(j>n):break;
    f=s
    s=t
    i=i+1
