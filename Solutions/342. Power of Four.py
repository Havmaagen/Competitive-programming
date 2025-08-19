class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        answer = (n > 0) and (n & (n - 1) == 0) and (n.bit_length() % 2 == 1)
        
        return answer