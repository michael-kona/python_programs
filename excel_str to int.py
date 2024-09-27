s=input()
c=0
for ch in s:
    c=c*26+(ord(ch)-ord('A')+1)
print(c)
