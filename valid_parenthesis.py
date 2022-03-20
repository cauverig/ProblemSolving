"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Solution:
    def is_valid(self, s):
        stack = ['N']
        m = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in m.keys():
                if stack.pop() != m[i]:
                    return False
            else:
                stack.append(i)

        return len(stack) == 1


if __name__ == '__main__':
    sol_obj = Solution()
    assert sol_obj.is_valid('(){}[]')
    assert sol_obj.is_valid(')') == False
