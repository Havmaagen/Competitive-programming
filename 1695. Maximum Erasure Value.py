class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        answer = 0
        window_sum = 0
        i = 0
        unique_values = set()
        for num in nums:
            while num in unique_values:
                window_sum -= nums[i]
                unique_values.remove(nums[i])
                i += 1
            
            window_sum += num
            unique_values.add(num)
            
            answer = max(window_sum, answer)
        
        return answer