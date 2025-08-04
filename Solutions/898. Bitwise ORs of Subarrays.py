class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        union = set()
        frontier = {0}
        for x in arr:
            frontier = {x | y for y in frontier} | {x}
            union |= frontier
        
        answer = len(union)
        
        return answer