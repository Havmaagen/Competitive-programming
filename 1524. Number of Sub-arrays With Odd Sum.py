class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        n = len(arr)
        answer = 0
        dp = 0
        for i in range(n):
            if arr[i] & 1 == 1:
                dp = i + 1 - dp
            answer += dp
        
        MOD = 10**9 + 7
        answer %= MOD
        
        return answer