class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        n = len(s)
        if n == 0:
            return 0
        
        s.sort(reverse=True)
        g.sort(reverse=True)
        
        count = 0
        for greed in g:
            if greed <= s[count]:
                count += 1
                if count == n:
                    break
        
        return count