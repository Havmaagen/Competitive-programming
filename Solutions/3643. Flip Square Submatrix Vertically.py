class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        i1, i2 = x, x + k - 1
        while i1 < i2:
            for j in range(y, y + k):
                grid[i1][j], grid[i2][j] = grid[i2][j], grid[i1][j]
            i1 += 1
            i2 -= 1
        
        return grid