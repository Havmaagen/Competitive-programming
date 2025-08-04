class Solution(object):
    def hasMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        left, right = p.split("*")
        n, n_left = len(s), len(left)
        idx_left = None
        for i in range(n):
            if s[i:i+n_left] == left:
                idx_left = i
                break
        else:
            return False
        
        return right in s[idx_left+n_left:]