# adapted from https://leetcode.com/discuss/59051/c-code-in-9-lines

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        start = -1
        max_length = 0
        symbol_index = [-1] * 256
        for i in range(len(s)):
            x = s[i]
            start = max(start, symbol_index[ord(x)])
            max_length = max(max_length, i - start)
            symbol_index[ord(x)] = i
        return max_length
