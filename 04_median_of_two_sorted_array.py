"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5


"""
import sys


def findMedianSortedArrays(nums1, nums2):
    total = len(nums1) + len(nums2)

    def helper(nums1, start1, nums2, start2, k):

        if start1 >= len(nums1):
            return nums2[start2 + k - 1]

        if start2 >= len(nums2):
            return nums1[start1 + k - 1]

        if k == 1:
            return min(nums1[start1], nums2[start2])

        index1 = start1 + k // 2 - 1
        index2 = start2 + k // 2 - 1
        key1 = nums1[index1] if index1 < len(nums1) else sys.maxsize
        key2 = nums2[index2] if index2 < len(nums2) else sys.maxsize

        if key1 < key2:
            return helper(nums1, start1 + k // 2, nums2, start2, k - k // 2)
        else:
            return helper(nums1, start1, nums2, start2 + k // 2, k - k // 2)

    if total % 2 == 1:
        return helper(nums1, 0, nums2, 0, total // 2 + 1)

    else:
        return (helper(nums1, 0, nums2, 0, total // 2) + helper(nums1, 0, nums2, 0, total // 2 + 1)) / 2.0
