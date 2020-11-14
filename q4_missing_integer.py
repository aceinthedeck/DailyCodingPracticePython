"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def missing_integer(array):

    n = len(array)
    # if array has [1..N] elements then the solution is n+1.
    # if array has num<=0 or num>=1 it means the solutions is <n 
    # replace any number less than 0 or greater than n with n+1 as solution is <n
    for i in range(n):
        if array[i]<=0 or array[i]>n:
            array[i] = n + 1
    

    for i in range(n):
        num = abs(array[i])

        if num > n:
            continue

        num = num - 1

        if array[num] > 0:
            array[num] = -1 * array[num]
        
    
    for i in range(n):
        if array[i] >= 0:
            return i+1
    
    return n+1
    
assert missing_integer([3, 4, -1, 1]) == 2
assert missing_integer([1, 2, 0]) == 3
assert missing_integer([1, 2, 5]) == 3
assert missing_integer([1]) == 2
assert missing_integer([-1, -2]) == 1
assert missing_integer([]) == 1

