class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        count = 0
        left, half_total = 0, (sum(nums) + 1) // 2
        for i in range(n - 1):
            left += nums[i]
            if left >= half_total:
                count += 1
        
        return count