class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        output = 0
        n, i = len(s), 0
        chars = set()
        for j in range(n):
            while s[j] in chars:
                chars.remove(s[i])
                i += 1
            
            chars.add(s[j])
            
            if j - i == 2:
                output += 1
                chars.remove(s[i])
                i += 1
        
        return output