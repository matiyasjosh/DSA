#to show the process Imma include the encryption process
#so the algorithm first takes the divisors of the length of string
#for example if we take the word leetcode it has the length of 8 and the divisors will be [1,2,4,8]
#so starting from the most significant number we will reverse the string from the beginning like; most significant is 8 so the whole word will be reversed edocteel
#then 4 so the first 4 words will be reversed as codeteel, after that 2 words will be reversed so it will be ocdeteel. lastly it is one which is negligible so the implementation for encryption goes as follows

#first line accept the length of the string and the second line accept the string itself
n = int(input())
s = input()

divisor = [j for j in range(2, n+1) if n%j==0]

def encrypt(s):
    for i in divisor[::-1]:
        sub_s = s[:i]
        rev_s = sub_s[::-1]
        s = rev_s + s[i:]
    return s

#to reverse the encryption all we need to do is start from the least significant divisor that is 2 in our example
#so it is the exact the same code but with tiny difference
def decrypt(s):
    for i in divisor:
        sub_s = s[:i]
        rev_s = sub_s[::-1]
        s = rev_s + s[i:]
    return s


print("when it is encrypted: ", encrypt(s))
print("when it is decrypted: ", decrypt(s))
