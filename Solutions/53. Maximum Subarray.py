class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        answer = nums[0]
        curr_max = 0
        for num in nums:
            curr_max = max(curr_max, 0) + num
            answer = max(answer, curr_max)
        
        return answer