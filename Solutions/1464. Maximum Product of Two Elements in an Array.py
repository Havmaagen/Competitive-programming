class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        first_max, second_max = None, None
        for num in nums:
            if first_max is None:
                first_max = num
            elif first_max < num:
                second_max, first_max = first_max, num
            elif (second_max is None) or (second_max < num):
                second_max = num
        
        output = (first_max - 1) * (second_max - 1)
        
        return output