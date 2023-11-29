#remove the the leftmost characters that are not in both string inputs and the right most strings has to be similar
#example s1="test" s2="west" then we remove t and w and the number of removed character is 2 so it returns 2
s=input()
t=input()

s,t=s[::-1],t[::-1] #reversing the string so that we can detect 
i=0 #we use it as an index

while i<len(s) and i<len(t):
    if s[i]==t[i]:
        i+=1
    else:
        break

print(len(s[i:])+len(t[i:]))
