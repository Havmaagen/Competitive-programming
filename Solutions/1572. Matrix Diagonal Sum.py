class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
        n = len(mat)
        output = sum(mat[i][i] + mat[i][n - i - 1] for i in range(n))
        if n % 2 == 1:
            center = n // 2
            output -= mat[center][center]
        
        return output