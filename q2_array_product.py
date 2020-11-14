"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def find_product(array):

    allProduct = 1
    for num in array:
        allProduct = allProduct*num
    
    result = []

    for num in array:
        result.append(allProduct/num)
    
    return result

assert find_product([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert find_product([3, 2, 1]) == [2, 3, 6]


def find_product_without_division(array):
    cumulative_product = 1
    right_prod_array = list()
    for num in array:
        cumulative_product *= num
        right_prod_array.append(cumulative_product)

    cumulative_product = 1
    left_prod_array = list()
    for num in array[::-1]:
        cumulative_product *= num
        left_prod_array.append(cumulative_product)
    left_prod_array = left_prod_array[::-1]
    output_array = list()
    for i in range(len(array)):
        num = None
        if i == 0:
            num = left_prod_array[i + 1]
        elif i == len(array) - 1:
            num = right_prod_array[i - 1]
        else:
            num = right_prod_array[i - 1] * left_prod_array[i + 1]
        output_array.append(num)
    
    return output_array

assert find_product_without_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert find_product_without_division([3, 2, 1]) == [2, 3, 6]

