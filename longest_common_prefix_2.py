"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


def longest_common_prefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest


if __name__ == '__main__':
    print(longest_common_prefix(["flower", "flow", "float"]))