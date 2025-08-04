class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        score = 0
        marked = (len(nums) + 1) * [False]
        
        heap = []
        for i, x in enumerate(nums):
            heapq.heappush(heap, (x, i))
        
        while heap:
            x, i = heapq.heappop(heap)
            if not marked[i]:
                score += x
                marked[i] = marked[i - 1] = marked[i + 1] = True
        
        return score