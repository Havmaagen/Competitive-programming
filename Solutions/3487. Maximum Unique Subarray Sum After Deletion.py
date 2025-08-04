class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        unique_nums = set()
        pos_sum = 0
        nonpos_sum = float("-inf")
        for num in nums:
            if num > 0:
                if num not in unique_nums:
                    pos_sum += num
                    unique_nums.add(num)
            elif num > nonpos_sum:
                nonpos_sum = num
        
        answer = pos_sum if (pos_sum > 0) else nonpos_sum
        
        return answer