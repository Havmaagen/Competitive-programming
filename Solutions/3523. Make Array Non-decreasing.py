class Solution(object):
    def maximumPossibleSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        answer = 0
        max_val = 0
        for num in nums:
            if num >= max_val:
                max_val = num
                answer += 1
        
        return answer