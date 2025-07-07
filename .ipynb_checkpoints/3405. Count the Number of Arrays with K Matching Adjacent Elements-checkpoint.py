class Solution(object):
    def countGoodArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        
        MOD = 10 ** 9 + 7
        
        if m == 1:
            answer = 1 if (k == n - 1) else 0
        else:
            answer = (m * pow(m - 1, n - k - 1, MOD)) % MOD
            answer = (self.binom(n - 1, k, MOD) * answer) % MOD
        
        return answer
    
    
    def binom(self, n, k, mod):
        numerator, denominator = 1, 1

        for i in range(1, k + 1):
            numerator = (numerator * (n - i + 1)) % mod
            denominator = (denominator * i) % mod
        
        inv_denominator = pow(denominator, mod - 2, mod)
        val = (numerator * inv_denominator) % mod
        
        return val