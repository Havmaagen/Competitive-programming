class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        
        n = len(startTime)
        t = sum(endTime[i] - startTime[i] for i in range(k))
        answer = (eventTime if (k == n) else startTime[k]) - t
        for i in range(k, n):
            t += (endTime[i] - startTime[i]) - (endTime[i - k] - startTime[i - k])
            T = (eventTime if (i == n - 1) else startTime[i + 1]) - endTime[i - k]
            answer = max(answer, T - t)
        
        return answer