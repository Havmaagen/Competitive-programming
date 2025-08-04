class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        output = 0
        odd_neg_count, min_abs_val = False, float("inf")
        for row in matrix:
            for val in row:
                output += abs(val)
                min_abs_val = min(min_abs_val, abs(val))
                odd_neg_count ^= (val < 0)
        
        if odd_neg_count:
            output -= 2 * min_abs_val
        
        return output