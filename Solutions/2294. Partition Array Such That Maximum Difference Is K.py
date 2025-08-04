class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort()
        
        n = len(nums)
        count = 1
        current = nums[0]
        for num in nums:
            if num - current > k:
                count += 1
                current = num
        
        return count