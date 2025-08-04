class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        answer = 0
        streak = 0
        max_val = 0
        for num in itertools.chain(nums, [0]):
            if num > max_val:
                max_val = num
                answer = 0
                streak = 1
            elif num == max_val:
                streak += 1
            else:
                answer = max(streak, answer)
                streak = 0
        
        return answer