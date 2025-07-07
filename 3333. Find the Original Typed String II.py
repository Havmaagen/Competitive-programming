class Solution(object):
    def possibleStringCount(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        
        MOD = 10**9 + 7
        n = len(word)
        
        freq = [1]
        for i in range(1, n):
            if word[i] == word[i - 1]:
                freq[-1] += 1
            else:
                freq.append(1)
        
        answer = 1
        for f in freq:
            answer = (answer * f) % MOD
        
        
        d = len(freq)
        if d >= k:
            return answer
        
        
        dp = k * [0]
        dp[0] = 1
        for i in range(d):
            edge = k - 1 - freq[i]
            dp[k - 1] = sum(dp[max(edge, 0):(k - 1)]) % MOD
            for j in range(k - 2, -1, -1):
                edge -= 1
                dp[j] = (dp[j + 1] - dp[j] + (dp[edge] if (edge >= 0) else 0)) % MOD
            
            dp[i] = 0
        
        answer = (answer - sum(dp)) % MOD
        
        return answer