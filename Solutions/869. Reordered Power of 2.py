class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        n_count = self.count_digits(n)
        answer = any(n_count == self.count_digits(1 << i) for i in range(30))
        
        return answer
    
    
    def count_digits(self, x):
        digits = 10 * [0]
        while x > 0:
            digits[x % 10] += 1
            x //= 10
        
        return digits