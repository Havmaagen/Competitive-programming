class Solution(object):
    def kthCharacter(self, k, operations):
        """
        :type k: int
        :type operations: List[int]
        :rtype: str
        """
        
        k -= 1
        bits = k.bit_length()
        shift = 0
        i = 0
        while i <= bits - 1:
            if k & operations[i]:
                shift += 1
            k >>= 1
            i += 1
        
        answer = chr(ord("a") + (shift % 26))
        
        return answer