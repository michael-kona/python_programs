def del_vowel(s):
    l=list(s)
    for c in s:
        if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
            l.remove(c)
    return "".join(l)
def insert_b4_consonant(s):
    l=list(s)
    n=len(l)
    i=0
    while i<n:
        if (l[i] not in '.aeiou') and (l[i-1]!='.' ):
            l.insert(i,'.')
            n=n+1
            i=i+2
    return "".join(l)
s=input()
s=s.lower()
s=del_vowel(s)
print(insert_b4_consonant(s))
