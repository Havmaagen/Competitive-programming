class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        events.sort()
        starts = [start for start, _, _ in events]
        
        n = len(events)
        dp = [(n + 1) * [0] for _ in range(k + 1)]
        for i in range(n - 1, -1, -1):
            j = bisect.bisect_left(starts, events[i][1] + 1, lo=i+1)
            for d in range(1, k + 1):
                dp[d][i] = max(dp[d][i + 1], events[i][2] + dp[d - 1][j])
        
        answer = dp[-1][0]
        
        return answer