s=input()
i=0
j=len(s)-1
while i<j:
    #print(s[i],'-',s[j])
    if not s[i].isalpha():#move index to next alphabhet forward
        for k in range(i+1,j):
            i=k
            if s[i].isalpha():
                break
    if not s[j].isalpha():#move index to next alphabhet backward
        for k in range(j-1,i,-1):
            j=k
            if s[j].isalpha():
                break 
    #print(s[i],'-',s[j])
    if(s[i].isalpha() and s[j].isalpha()):#swapping
        s=s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
    i=i+1
    j=j-1
print(s)
