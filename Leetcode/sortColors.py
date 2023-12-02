"""
This is a solution for leetcode problem with the following link address "https://leetcode.com/problems/sort-colors/description/".
It help to see some of easy inplace sorting algoritms. In this problem insertion sort is used
"""

def insertionSort(nums):
    for i in range(1,len(nums)):
        while i>0 and nums[i]<nums[i-1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i-=1
