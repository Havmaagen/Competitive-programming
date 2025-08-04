class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        first_idx, last_idx = 26 * [-1], 26 * [-1]
        for i, char in enumerate(s):
            j = ord(char) - ord("a")
            if first_idx[j] == -1:
                first_idx[j] = i
            last_idx[j] = i
        
        count = sum(len(set(s[i+1:j])) for i, j in zip(first_idx, last_idx) if i != -1)
        
        return count