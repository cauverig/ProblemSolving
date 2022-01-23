"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

