"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
"""


def isSymmetric(root):
    def helper(left, right):

        if left is None and right is None:
            return True

        if left is not None and right is not None:
            return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)

        else:
            return False

    if root is None:
        return True

    else:
        return helper(root.left, root.right)
