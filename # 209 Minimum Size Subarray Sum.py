class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0
        n = len(nums)
        subarray_end_index = [-1] * n
        subarray_sum = [0] * n
        
        # init
        for i in range(n):
            subarray_end_index[0] = i + 1
            subarray_sum[0] += nums[i]
            if subarray_sum[0] >= s:
                break

        # loop
        for i in range(1, n):
            subarray_end_index[i] = subarray_end_index[i - 1]
            subarray_sum[i] = subarray_sum[i - 1] - nums[i - 1]
            if subarray_sum[i] >= s:
                continue
            else:
                for j in range(subarray_end_index[i], n):
                    subarray_end_index[i] = j + 1
                    subarray_sum[i] += nums[j]
                    if subarray_sum[i] >= s:
                        break
                if subarray_sum[i] < s:
                    # can't find end_index
                    subarray_end_index[i] = -1
                    break

        min_length = subarray_end_index[0]
        for i in range(n):
            if subarray_end_index[i] == -1:
                break
            else:
                min_length = min(min_length, subarray_end_index[i] - i)
                
        return min_length    
        
