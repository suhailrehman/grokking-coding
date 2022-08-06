from typing import List
import math

"""
Given an array of positive numbers and a positive number 'S', find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0 if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
Example 2:

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] 
or [1, 1, 6].


Code Walkthrough

[2, 1, 5, 2, 3, 2] ; S = 7
          s  i

min_size = 6
w_size = 0
w_sum = 0
w_start = 0

i=4; w_sum=7, w_size=2 w_start=2

min_size=2

"""
def smallest_subarray_sum(nums: List[int], S: int) -> int:
    min_size = math.inf
    w_size = 0
    w_sum = 0
    w_start = 0

    for i in len(nums):
        w_sum += nums[i]
        while w_sum >= S:
            if w_size < min_size:
                min_size = w_size
            w_sum -= nums[w_start]
            w_size -= 1
            w_start += 1
    if min_size == math.inf:
        return 0        
    return min_size