class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        d = {}
        for i, num in enumerate(sorted(nums)):
            if num not in d:
                d[num] = i
        output = [d[num] for num in nums]
        
        return output