class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        answer = max(abs(nums[i] - nums[i - 1]) for i in range(n))
        
        return answer