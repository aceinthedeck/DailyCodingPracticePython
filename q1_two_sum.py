"""
Given a list of numbers, return whether any two sums to k. For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def two_sum(array, k):
    map = set()

    for num in array:
        if num in map:
            return True
        map.add(k-num)
    
    return False

assert not two_sum([],17)
assert two_sum([10, 15, 3, 7], 17)
assert not two_sum([10, 15, 3, 4], 17)