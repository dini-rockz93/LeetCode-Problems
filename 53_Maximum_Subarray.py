"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.

"""


def max_sub_array(array):

    max_final = array[0]
    max_current = array[0]

    for i in range(1, len(array)):

        max_current = max(array[i], array[i] + max_current)
        max_final = max(max_current, max_final)

    return max_final


array1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub_array(array1))
