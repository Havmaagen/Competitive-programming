class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        
        for fruit in fruits:
            for i, basket in enumerate(baskets):
                if basket >= fruit:
                    baskets.pop(i)
                    break
        
        answer = len(baskets)
        
        return answer