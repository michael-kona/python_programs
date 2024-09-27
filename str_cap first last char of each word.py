s=input()
for i in range(len(s)):
    if i==0 or i==len(s)-1:
        if ord(s[i])>=97 and ord(s[i])<=122:
            s=s[:i]+chr(ord(s[i])-32)+s[i+1:]
    if s[i]==" " and ord(s[i-1])>=97 and ord(s[i-1])<=122 and (i-1)>0:
            s=s[:i-1]+chr(ord(s[i-1])-32)+s[i:]
    if s[i]==" " and ord(s[i+1])>=97 and ord(s[i+1])<=122 and i+1<=len(s)-1:
                s=s[:i+1]+chr(ord(s[i+1])-32)+s[i+2:]
print(s)
