# You are using Python
def sumOfDigits(num):
    s=0
    while num!=0:
        s=s+num%10
        num=num//10
    return s
n=int(input())
print(sumOfDigits(n))
