class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = [nums[num] for num in nums]
        
        return ans