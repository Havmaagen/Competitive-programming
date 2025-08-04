class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, y - x)
        
        output = -heapq.heappop(heap) if (len(heap) == 1) else 0
        
        return output