class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        prefix = 0
        min_val, max_val = 0, 0
        for num in nums:
            prefix += num
            if prefix < min_val:
                min_val = prefix
            elif prefix > max_val:
                max_val = prefix
        
        answer = max_val - min_val
        
        return answer