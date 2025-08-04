class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        
        events.sort()
        
        n = len(events)
        minDay = events[0][0]
        maxDay = max(end for _, end in events)
        
        count = 0
        j = 0
        queue = []
        
        for i in range(minDay, maxDay + 1):
            while (j < n) and (events[j][0] <= i):
                heapq.heappush(queue, events[j][1])
                j += 1
            
            while queue and (queue[0] < i):
                heapq.heappop(queue)
            
            if queue:
                heapq.heappop(queue)
                count += 1
        
        return count