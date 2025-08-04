class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        
        distances = [[] for _ in range(rows + cols - 1)]
        for i, j in product(range(rows), range(cols)):
            d = abs(i - rCenter) + abs(j - cCenter)
            distances[d].append([i, j])
        
        output = [pair for array in distances for pair in array]
        
        return output