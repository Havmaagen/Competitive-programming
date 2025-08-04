class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n = len(grid)
        for i in range(n):
            if grid[i].count(1) == n - 1:
                return i