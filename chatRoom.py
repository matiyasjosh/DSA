#check if there is "hello" in the string 
def check(s):
    hello="hello"
    index=0
    
    for char in s:
        if char==hello[index]:
            index+=1
            if index==len(hello):
                return "YES"
    return "NO"

s=input()
print(check(s))
