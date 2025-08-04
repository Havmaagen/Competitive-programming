class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                
                total_value = 0
                island = deque([(i, j)])
                while island:
                    i0, j0 = island.pop()
                    total_value += grid[i0][j0]
                    grid[i0][j0] = 0
                    for step in {-1, 1}:
                        h = i0 + step
                        if (0 <= h < m) and (grid[h][j0] != 0):
                            island.append((h, j0))
                        
                        v = j0 + step
                        if (0 <= v < n) and (grid[i0][v] != 0):
                            island.append((i0, v))
                
                if total_value % k == 0:
                    count += 1
        
        return count