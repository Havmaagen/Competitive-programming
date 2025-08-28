class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        
        n = len(grid)
        for i in range(n):
            diag = [grid[i + j][j] for j in range(n - i)]
            diag.sort(reverse=True)
            for j in range(n - i):
                grid[i + j][j] = diag[j]
        
        for j in range(1, n):
            diag = [grid[i][i + j] for i in range(n - j)]
            diag.sort()
            for i in range(n - j):
                grid[i][i + j] = diag[i]
        
        return grid