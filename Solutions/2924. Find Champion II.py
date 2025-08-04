class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        champions = set(range(n)) - {v for u, v in edges}
        output = champions.pop() if (len(champions) == 1) else -1
        
        return output