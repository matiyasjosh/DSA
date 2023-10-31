"""
returns the number of boat that is required so that their weight doesn't exceed the limit
Initially I sorted the list so that I can use two pointers technique to solve this problem which makes it easier 
"""

def boat(pepa, limit):
    pepa.sort()
    left, right = 0, len(pepa)-1
    Boat = 0
    while left<=right:
        if left!=right:
            if pepa[left]+pepa[right]<=limit:
                Boat+=1
                left+=1
                right-=1
            elif pepa[left]+pepa[right]>limit:
                Boat+=1
                right-=1                         
        else:
            Boat+=1
            left+=1
    return Boat


print(boat([3,2,2,1], 3))
print(boat([3,5,3,4], 5))
