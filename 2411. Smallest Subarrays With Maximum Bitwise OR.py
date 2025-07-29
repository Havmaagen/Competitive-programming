class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        n_bits = max(max(nums).bit_length(), 1)
        answer = n * [0]
        bit_pos = n_bits * [-1]
        for i in range(n - 1, -1, -1):
            for j in range(n_bits):
                if nums[i] & (1 << j):
                    bit_pos[j] = i
            
            answer[i] = max(max(bit_pos) - (i - 1), 1)
        
        return answer