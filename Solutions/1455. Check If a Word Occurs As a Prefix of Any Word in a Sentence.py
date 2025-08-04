class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        
        for i, s in enumerate(sentence.split(), 1):
            if s.startswith(searchWord):
                return i
        else:
            return -1