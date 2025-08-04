class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d = defaultdict(int)
        for char in s:
            d[char] += 1
        
        a1, a2 = 0, len(s)
        for char in d:
            if d[char] % 2 == 1:
                a1 = max(a1, d[char])
            else:
                a2 = min(a2, d[char])
        
        answer = a1 - a2
        
        return answer