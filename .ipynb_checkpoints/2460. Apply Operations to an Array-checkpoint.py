class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n, w = len(nums), 0
        for i in range(n):
            if nums[i] == 0:
                continue
            
            if (i < n - 1) and (nums[i] == nums[i + 1]):
                nums[i] *= 2
                nums[i + 1] = 0
            
            nums[w], nums[i] = nums[i], nums[w]
            w += 1
        
        return nums