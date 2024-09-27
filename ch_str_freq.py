s=input()
ch=input()
c=0
for i in range(len(s)):
    if s[i]==ch:
        c=c+1
print("Frequency of {0} = {1}".format(ch,c))
