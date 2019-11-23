"""

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

"""


def isvalid(string):

    open_brackets = "{[("
    close_brackets = "]})"
    pair_brackets = {
        '}': '{',
        ')': '(',
        ']': '['
    }

    stack = []
    for char in string:

        if char in open_brackets:
            stack.append(char)
        elif char in  close_brackets:
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == pair_brackets[char]:
                    stack.pop()
                else:
                    return False
    return len(stack) == 0


str1 = ""
if isvalid(str1):
    print("valid brackets")
else:
    print("not a valid brackets")
