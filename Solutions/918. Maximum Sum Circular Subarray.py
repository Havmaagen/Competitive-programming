class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total_sum = 0
        max_sum, min_sum = nums[0], nums[0]
        max_curr, min_curr = 0, 0
        for num in nums:
            total_sum += num
            
            max_curr = max(max_curr, 0) + num
            max_sum = max(max_sum, max_curr)
            
            min_curr = min(min_curr, 0) + num
            min_sum = min(min_sum, min_curr)
        
        answer = max_sum
        if min_sum != total_sum:
            answer = max(answer, total_sum - min_sum)
        
        return answer