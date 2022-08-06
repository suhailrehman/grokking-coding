from typing import List

"""
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].


n=5
w_size = 2
w_sum = 4
max_sum = 7


i = 2 - 2 +1 = 1


2,3,4,1,5   

"""

def max_subarray_size_k(nums: List[int], k: int) -> int:
    n = len(nums)
    w_size = 0
    w_sum = 0
    max_sum = 0

    for i in range(n):    # i = 2
        if w_size < k:  # yes
            w_sum += nums[i] 
            w_size += 1
        if w_size == k: # yes
            if w_sum > max_sum:
                max_sum = w_sum
            w_sum -= nums[i-k+1]
            w_size -= 1

    return max_sum      

# Test Cases

nums = [2, 1, 5, 1, 3, 2]
k=3 
print(max_subarray_size_k(nums,k))

nums = [2, 3, 4, 1, 5]
k=2 
print(max_subarray_size_k(nums,k))
