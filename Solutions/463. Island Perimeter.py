class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += 4
                    if (i >= 1) and (grid[i - 1][j] == 1):
                        perimeter -= 2
                    if (j >= 1) and (grid[i][j - 1] == 1):
                        perimeter -= 2
        
        return perimeter