class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        MOD = 10**9 + 7
        
        nums.sort()
        
        n = len(nums)
        i, j = 0, n - 1
        count = pow(2, j - i, MOD)
        inv = pow(2, MOD - 2, MOD)
        answer = 0
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                answer += count
                i += 1
            count = (count * inv) % MOD
        
        answer %= MOD
        
        return answer