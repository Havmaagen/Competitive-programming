class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        freq = defaultdict(int)
        for x in arr:
            freq[x] += 1
        
        answer = -1
        for x in freq:
            if (x == freq[x]) and (x > answer):
                answer = x
        
        return answer