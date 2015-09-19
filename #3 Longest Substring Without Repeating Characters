class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        symbol_index = dict()
        previous_duplicate_index = []
        for i in range(len(s)):
            x = s[i]
            if x not in symbol_index:
                previous_duplicate_index.append(-1)
                symbol_index[x] = i
            else:
                previous_duplicate_index.append(symbol_index[x])
                symbol_index[x] = i
        print previous_duplicate_index
        max_length = 0
        left = right = 0
        for i in range(len(s)):
            if previous_duplicate_index[i] < left:
                right = i + 1
            else:
                left = previous_duplicate_index[i] + 1
                right = i + 1
            max_length = max(max_length, right - left)
        return max_length
