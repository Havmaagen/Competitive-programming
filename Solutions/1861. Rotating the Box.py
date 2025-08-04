class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        
        m, n = len(box), len(box[0])
        result = [m * ["."] for _ in range(n)]
        for i in range(m):
            k = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] == "*":
                    result[j][m - i - 1] = "*"
                    k = j - 1
                elif box[i][j] == "#":
                    result[k][m - i - 1] = "#"
                    k -= 1
        
        return result