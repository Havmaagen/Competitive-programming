class Solution(object):
    def maxArea(self, coords):
        """
        :type coords: List[List[int]]
        :rtype: int
        """
        
        dx, dy = {}, {}
        x_min, x_max = 10 ** 6, 0
        y_min, y_max = 10 ** 6, 0
        for x, y in coords:
            if x in dx:
                if y < dx[x][0]:
                    dx[x][0] = y
                elif y > dx[x][1]:
                    dx[x][1] = y
            else:
                dx[x] = [y, y]
                x_min = min(x_min, x)
                x_max = max(x_max, x)
            
            if y in dy:
                if x < dy[y][0]:
                    dy[y][0] = x
                elif x > dy[y][1]:
                    dy[y][1] = x
            else:
                dy[y] = [x, x]
                y_min = min(y_min, y)
                y_max = max(y_max, y)
        
        answer = 0
        for x in dx:
            s = max(abs(x_min - x), abs(x_max - x)) * (dx[x][1] - dx[x][0])
            answer = max(answer, s)
        for y in dy:
            s = max(abs(y_min - y), abs(y_max - y)) * (dy[y][1] - dy[y][0])
            answer = max(answer, s)
        
        answer = answer if (answer > 0) else -1
        
        return answer