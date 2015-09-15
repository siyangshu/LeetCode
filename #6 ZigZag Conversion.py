class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == '':
            return ''
        if numRows == 1:
            return s
        n = numRows
        li = [[] for x in range(n)] # should not use [[]] * n because it's shallow copy
        for index_in_s in range(len(s)):
        	list_index = index_in_s % (2 * n - 2)
        	if list_index > n - 1:
        		list_index = 2 * n - 2 - list_index
        	li[list_index].append(s[index_in_s])
        str_return = ''
        for x in li:
        	str_return += ''.join(x)
        return str_return
