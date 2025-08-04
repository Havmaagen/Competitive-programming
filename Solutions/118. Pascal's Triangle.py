class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        triangle = [[1]]
        for i in range(1, numRows):
            row = [(triangle[-1][j - 1] + triangle[-1][j]) if (0 < j < i) else 1 for j in range(i + 1)]
            triangle.append(row)
        
        return triangle