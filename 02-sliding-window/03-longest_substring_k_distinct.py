from typing import List

"""
Problem Statement

Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".


Sliding window with set to keep track of distinct characters.
Grow window on one side
if > K distinct characters, shrink until less than K
store longest substring

"""


def longest_substring_k_distinct(string: str, k: int) -> int:
    w_start = 0
    w_end = 0
    max_size = 0
    w_set = set()
    
    for w_end in range(len(string)):
        w_set.add(string[i])
        if len(w_set) <= k:
            max_size = max(max_size, w_end - w_start)
        
        while len(w_set) > k:
            w_set.remove(string[w_start])
            w_start +=1

    return max_size
                