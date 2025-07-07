class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        answer = -1
        min_val = nums[0]
        for i in range(1, n):
            if nums[i] > min_val:
                answer = max(answer, nums[i] - min_val)
            else:
                min_val = nums[i]
        
        return answer