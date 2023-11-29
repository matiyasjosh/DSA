#I tried to solve this problem using the stack data structure concept
#the problem is to remove a star and character that locates at the left of the star

class solutioN:
    def rmvStars(s:str)->str:
        stack=[]
        for c in s:
            if c=="*" and stack and stack[-1]!="*":
                s.pop()
            else:
                s.append(c)
        return "".join(stack)

#the following class can be implemented as
obj=solutioN()
s="erase*****"
print(obj.rmvStars(s))  # which returns ""
