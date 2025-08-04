class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums) // 3
        
        heap1 = [-nums[i] for i in range(n)]
        heapq.heapify(heap1)
        
        prefix = (n + 1) * [0]
        prefix[0] = -sum(heap1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1]
            if nums[n + i - 1] < -heap1[0]:
                prefix[i] += nums[n + i - 1] + heapq.heappop(heap1)
                heapq.heappush(heap1, -nums[n + i - 1])
        
        heap2 = nums[(2 * n):]
        heapq.heapify(heap2)
        
        suffix = (n + 1) * [0]
        suffix[-1] = sum(heap2)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1]
            if nums[n + i] > heap2[0]:
                suffix[i] += nums[n + i] - heapq.heappop(heap2)
                heapq.heappush(heap2, nums[n + i])
        
        answer = min(prefix[i] - suffix[i] for i in range(n + 1))
        
        return answer