class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        
        counter0 = defaultdict(int)
        for s in chars:
            counter0[s] += 1
        
        output = 0
        for word in words:
            counter = defaultdict(int)
            for s in word:
                counter[s] += 1
            
            for s in counter:
                if counter[s] > counter0[s]:
                    break
            else:
                output += len(word)
        
        return output