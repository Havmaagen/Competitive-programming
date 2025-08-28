class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        
        m, n = len(mat), len(mat[0])
        answer = []
        i, j = 0, 0
        upwards = True
        while (i < m) and (j < n):
            answer.append(mat[i][j])
            
            if upwards:
                ni, nj = i - 1, j + 1
            else:
                ni, nj = i + 1, j - 1
            
            if (0 <= ni < m) and (0 <= nj < n):
                i, j = ni, nj
            else:
                upwards = not upwards
                if upwards:
                    if i < m - 1:
                        i += 1
                    else:
                        j += 1
                else:
                    if j < n - 1:
                        j += 1
                    else:
                        i += 1
        
        return answer