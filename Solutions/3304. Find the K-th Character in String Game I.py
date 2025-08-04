class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        
        shift = bin(k - 1).count("1")
        answer = chr(ord("a") + (shift % 26))
        
        return answer