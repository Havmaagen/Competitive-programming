class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        
        meetings.sort()
        
        counts = n * [0]
        vacant, occupied = list(range(n)), []
        for start, end in meetings:
            while occupied and (occupied[0][0] <= start):
                _, i = heapq.heappop(occupied)
                heapq.heappush(vacant, i)
            
            if vacant:
                i = heapq.heappop(vacant)
            else:
                prev_end, i = heapq.heappop(occupied)
                end = prev_end + (end - start)
            
            heapq.heappush(occupied, (end, i))
            counts[i] += 1
        
        answer = 0
        max_count = 0
        for i, count in enumerate(counts):
            if count > max_count:
                max_count = count
                answer = i
        
        return answer