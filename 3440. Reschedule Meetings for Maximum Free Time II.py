class Solution(object):
    def maxFreeTime(self, eventTime, startTime, endTime):
        """
        :type eventTime: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        
        n = len(startTime)
        max_free = 0
        bwd, fwd = 0, 0
        for i in range(n):
            bwd_before = startTime[i] - (0 if (i == 0) else endTime[i - 1])
            bwd_after = (eventTime if (i == n - 1) else startTime[i + 1]) - endTime[i]
            bwd_duration = endTime[i] - startTime[i]
            if bwd_duration <= bwd:
                bwd_total = bwd_before + bwd_after + bwd_duration
            else:
                bwd_total = bwd_before + bwd_after
            bwd = max(bwd, bwd_before)
            
            j = n - 1 - i
            fwd_before = startTime[j] - (0 if (j == 0) else endTime[j - 1])
            fwd_after = (eventTime if (j == n - 1) else startTime[j + 1]) - endTime[j]
            fwd_duration = endTime[j] - startTime[j]
            if fwd_duration <= fwd:
                fwd_total = fwd_before + fwd_after + fwd_duration
            else:
                fwd_total = fwd_before + fwd_after
            fwd = max(fwd, fwd_after)
            
            max_free = max(max_free, bwd_total, fwd_total)
        
        return max_free