class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        n = len(word)
        answer = 1
        for i in range(1, n):
            if word[i] == word[i - 1]:
                answer += 1
        
        return answer