class Solution(object):
    def countPathsWithXorValue(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        
        dp = [[16 * [0] for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]] = 1
        for d in range(1, m + n - 1):
            i_min, i_max = max(d - n + 1, 0), min(d, m - 1) + 1
            for i in range(i_min, i_max):
                j = d - i
                x = grid[i][j]
                if i - 1 >= 0:
                    for y in range(16):
                        dp[i][j][x ^ y] += dp[i - 1][j][y]
                if j - 1 >= 0:
                    for y in range(16):
                        dp[i][j][x ^ y] += dp[i][j - 1][y]
        
        return dp[m - 1][n - 1][k] % mod