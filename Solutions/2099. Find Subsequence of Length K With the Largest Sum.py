class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        heap = []
        for i, num in enumerate(nums):
            if i < k:
                heappush(heap, (num, i))
            else:
                heappushpop(heap, (num, i))
        
        array = [num for num, _ in sorted(heap, key=lambda x: x[1])]
        
        return array