class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        
        n = len(nums)
        answer = []
        r = 0
        for i in range(n):
            if nums[i] == key:
                l, r = max(i - k, r), min(i + k + 1, n)
                answer.extend(range(l, r))
        
        return answer