s=input()
f=0
i=0
j=len(s)-1

while i<j:
    if s[i]!=s[j]:
        f=1
        break
    i=i+1
    j=j-1
if f==0:
    print("Palindrome")
else:
    print("Not a Palindrome")
