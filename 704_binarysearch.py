"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search
target in nums. If target exists, then return its index, otherwise return -1.

"""


def search(nums, target):

    l = 0
    r = len(nums) - 1

    while l <= r:

        mid = l + (r - l) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            l = mid + 1

        else:
            r = mid - 1

    return -1


arr = [1, 3, 5, 6, 7, 20]
value = 5
print(search(arr, value))