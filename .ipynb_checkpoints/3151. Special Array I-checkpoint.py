class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        n = len(nums)
        if n == 1:
            return True
        else:
            return all((nums[i] % 2) ^ (nums[i - 1] % 2) for i in range(1, n))