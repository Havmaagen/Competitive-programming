class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        answer = ((n > 0) and (n & (n - 1) == 0))
        
        return answer