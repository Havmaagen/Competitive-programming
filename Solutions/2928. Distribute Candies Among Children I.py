class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        
        count = 0
        for i in range(limit + 1):
            for j in range(limit + 1):
                if 0 <= n - i - j <= limit:
                    count += 1
        
        return count