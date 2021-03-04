"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

from typing import Dict


def longest_substring(str, k):

    max_length = 0

    str_map = dict()

    if not str:
        return max_length
    
    window_start = 0

    for window_end in range(len(str)):

        current_char = str[window_end]

        if current_char in str_map:
            window_start = max(window_start, str_map[current_char]+1)
        
        str_map[current_char] = window_end
        max_length = max(max_length, window_end-window_start+1)
    
    return max_length

# print(longest_substring("aabccbb",2))

assert longest_substring("abcba", 2) == 3