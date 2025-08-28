class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        
        max_area = 0
        max_diag2 = 0
        for a, b in dimensions:
            diag2 = a**2 + b**2
            if diag2 > max_diag2:
                max_area = a * b
                max_diag2 = diag2
            elif diag2 == max_diag2:
                max_area = max(max_area, a * b)
        
        return max_area