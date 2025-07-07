class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        
        freq = defaultdict(int)
        for x in word:
            freq[x] += 1
        
        answer = len(word)
        for x in freq:
            count = 0
            for y in freq:
                if freq[y] < freq[x]:
                    count += freq[y]
                elif freq[y] > freq[x] + k:
                    count += freq[y] - freq[x] - k
            
            answer = min(answer, count)
        
        return answer