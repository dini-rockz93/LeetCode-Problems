"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Two methods

1. sort the array and one pass
2. using hash tables

"""

# 1. sort the array and one pass


def two_sum(nums, target: int):
    """
    :param nums: list
    :type target: int
    """
    nums.sort()
    low = 0
    high = len(nums) - 1

    while low < high:

        current_sum = nums[low] + nums[high]

        if current_sum == target:

            return [nums[low], nums[high]]

        elif current_sum < target:
            low += 1

        else:
            high -= 1

    return [-1, -1]


# 2. using hash maps

def two_sum_hash(nums, target):

    hashmap = {}

    for i, num in enumerate(nums):

        current_sum = target - num

        if current_sum in hashmap:
            return sorted([current_sum, nums[i]])

        else:
            hashmap[num] = i


array = [7, 5, 1, 2, 3]
target = 6
print(two_sum_hash(array, target))
