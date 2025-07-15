class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        intervals.sort(key=lambda x: x[1])
        
        answer = 0
        prev = intervals[0][0]
        for start, end in intervals:
            if start >= prev:
                prev = end
            else:
                answer += 1
        
        return answer