class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        
        bmax = defaultdict(int)
        for word in words2:
            b = defaultdict(int)
            for char in word:
                b[char] += 1
            
            for char in b:
                bmax[char] = max(bmax[char], b[char])
        
        answer = []
        for word in words1:
            a = defaultdict(int)
            for char in word:
                a[char] += 1
            
            if all(bmax[char] <= a[char] for char in bmax):
                answer.append(word)
        
        return answer