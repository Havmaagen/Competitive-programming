class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        
        def comb2(n):
            return (n * (n - 1) / 2) if (n >= 2) else 0
        
        count = comb2(n + 2)
        count -= 3 * comb2(n - (limit + 1) + 2)
        count += 3 * comb2(n - 2 * (limit + 1) + 2)
        count -= comb2(n - 3 * (limit + 1) + 2)
        
        return count