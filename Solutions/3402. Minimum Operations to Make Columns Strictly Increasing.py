class Solution(object):
    def minimumOperations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(1, m):
            for j in range(n):
                if grid[i - 1][j] >= grid[i][j]:
                    count += grid[i - 1][j] - grid[i][j] + 1
                    grid[i][j] = grid[i - 1][j] + 1
        
        return count