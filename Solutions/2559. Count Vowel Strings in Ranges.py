class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        vowels = {"a", "e", "i", "o", "u"}
        n = len(words)
        prefix = (n + 1) * [0]
        for i, word in enumerate(words):
            prefix[i + 1] = prefix[i]
            if (word[0] in vowels) and (word[-1] in vowels):
                prefix[i + 1] += 1
        
        answer = [prefix[j + 1] - prefix[i] for i, j in queries]
        
        return answer