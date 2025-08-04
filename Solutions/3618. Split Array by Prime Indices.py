class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        diff = 0
        for i, num in enumerate(nums):
            diff += num if (i in PRIMES) else -num
        
        answer = abs(diff)
        
        return answer


def sieve(n):
    is_prime = (n + 1) * [True]
    is_prime[0], is_prime[1] = False, False
    d = int(n ** 0.5) + 1
    for i in range(2, d):
        if is_prime[i]:
            for j in range(i ** 2, n + 1, i):
                is_prime[j] = False
    
    primes = {i for i in range(n + 1) if is_prime[i]}
    
    return primes


N = 10 ** 5
PRIMES = sieve(N)