#program to find whether the given int is inside/outside of
#given range
def test_range(n1,n2,n):
    if(n>=n1 and n<=n2):
        print("Inside")
    else:
        print("Outside")
a=int(input())
b=int(input())
c=int(input())
test_range(a,b,c)
