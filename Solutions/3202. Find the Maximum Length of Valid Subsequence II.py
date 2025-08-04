class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        answer = 0
        for i in range(k):
            dp = k * [0]
            for num in nums:
                res = num % k
                dp[res] = dp[(i - res) % k] + 1
            
            answer = max(answer, max(dp))
        
        return answer