class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            while (i < j) and (nums[i] % 2 == 0):
                i += 1
            while (i < j) and (nums[j] % 2 == 1):
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        return nums