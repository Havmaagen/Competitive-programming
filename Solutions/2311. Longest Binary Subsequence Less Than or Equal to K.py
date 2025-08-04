class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        bits = k.bit_length()
        num = 0
        count = 0
        for i, char in enumerate(s[::-1]):
            if char == "1":
                if (i < bits) and (num + (1 << i) <= k):
                    num += 1 << i
                    count += 1
            else:
                count += 1
        
        return count