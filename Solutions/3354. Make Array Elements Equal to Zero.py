class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        prefix = (n + 1) * [0]
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        output = 0
        starts = [i for i, x in enumerate(nums) if x == 0]
        for i in starts:
            left, right = prefix[i], prefix[-1] - prefix[i + 1]
            output += max(2 - abs(left - right), 0)
        
        return output