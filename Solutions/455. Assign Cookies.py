class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        g.sort()
        s.sort()
        
        n = len(g)
        count = 0
        for size in s:
            if g[count] <= size:
                count += 1
                if count == n:
                    break
        
        return count