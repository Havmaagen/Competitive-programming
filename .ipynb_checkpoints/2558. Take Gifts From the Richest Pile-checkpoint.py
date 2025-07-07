class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        
        heap = [-x for x in gifts]
        heapq.heapify(heap)
        for _ in range(k):
            heapq.heapreplace(heap, -int(sqrt(-heap[0])))
        
        return -sum(heap)