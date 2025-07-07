class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        left, right = 0, sum(nums) - nums[0]
        
        if left == right:
            return 0
        
        for i in range(1, n):
            left += nums[i - 1]
            right -= nums[i]
            if left == right:
                return i
        
        return -1