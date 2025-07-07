class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        dp = [nums[0]]
        for i in range(1, n):
            j = bisect.bisect_left(dp, nums[i])
            if j < len(dp):
                dp[j] = nums[i]
            else:
                dp.append(nums[i])
        
        return len(dp)