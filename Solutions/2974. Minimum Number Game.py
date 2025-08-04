class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums.sort()
        arr = [num for i in range(0, len(nums), 2) for num in nums[i:i+2][::-1]]
        
        return arr