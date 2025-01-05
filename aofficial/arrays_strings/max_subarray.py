
import sys

def maxSubArray(nums):
    max_sum = float('-inf')
    curr_sum = 0
    for i, num in enumerate(nums):
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
