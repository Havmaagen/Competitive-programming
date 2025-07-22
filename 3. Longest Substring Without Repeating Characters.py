class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        answer = 0
        n = len(s)
        i, j = 0, 0
        unique_values = set()
        while j < n:
            while s[j] in unique_values:
                unique_values.remove(s[i])
                i += 1
            
            unique_values.add(s[j])
            answer = max(j - i + 1, answer)
            j += 1
        
        return answer