class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        prev = nums[0]
        count = 0
        for i in range(1, n - 1):
            if nums[i] == nums[i + 1]:
                continue
            
            if (prev < nums[i] > nums[i + 1]) or (prev > nums[i] < nums[i + 1]):
                count += 1
            
            prev = nums[i]
        
        return count