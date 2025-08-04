class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        score, ones = 0, 0
        max_score = -1
        for i in range(len(s) - 1):
            if s[i] == "0":
                score += 1
            else:
                score -= 1
                ones += 1
            max_score = max(max_score, score)
        
        ones += 1 * (s[-1] == "1")
        max_score += ones
        
        return max_score