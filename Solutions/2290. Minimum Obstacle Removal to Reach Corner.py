class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])
        start, end = (0, 0), (m - 1, n - 1)
        distance = [n * [-1] for _ in range(m)]
        distance[start[0]][start[1]] = 0
        vertices = deque([start])
        while vertices:
            i, j = vertices.popleft()
            for k in {-1, 1}:
                if (0 <= i + k < m) and (distance[i + k][j] == -1):
                    distance[i + k][j] = distance[i][j] + grid[i + k][j]
                    if grid[i + k][j] == 0:
                        vertices.appendleft((i + k, j))
                    else:
                        vertices.append((i + k, j))
                if (0 <= j + k < n) and (distance[i][j + k] == -1):
                    distance[i][j + k] = distance[i][j] + grid[i][j + k]
                    if grid[i][j + k] == 0:
                        vertices.appendleft((i, j + k))
                    else:
                        vertices.append((i, j + k))
        
        output = distance[end[0]][end[1]]
        
        return output