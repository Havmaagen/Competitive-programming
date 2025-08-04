class Solution(object):
    def maximumMedianSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        n = len(nums)
        answer = sum(nums[(n // 3)::2])
        
        return answer