"""
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the
result is returned.
"""
def sqrt(x):

    if x <= 1:
        return x

    low = 0
    high = x

    ans = 0

    while high >= low:

        mid = low + (high - low) // 2

        if mid * mid == x:
            return mid

        elif mid * mid < x:
            low = mid + 1
            ans = mid

        else:
            high = mid - 1
    return ans


x1 = 10000
print(sqrt(x1))
