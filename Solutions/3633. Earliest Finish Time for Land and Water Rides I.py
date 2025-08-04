class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        
        n1 = len(landStartTime)
        n2 = len(waterStartTime)
        
        end1 = min(landStartTime[i] + landDuration[i] for i in range(n1))
        end2 = min(waterStartTime[i] + waterDuration[i] for i in range(n2))
        
        time1 = min(max(waterStartTime[i], end1) + waterDuration[i] for i in range(n2))
        time2 = min(max(landStartTime[i], end2) + landDuration[i] for i in range(n1))
        answer = min(time1, time2)
        
        return answer