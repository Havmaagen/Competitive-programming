class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n_odd, n_even, n_change = 0, 0, 1
        prev_parity = nums[0] & 1
        for num in nums:
            parity = num & 1
            
            if parity == 1:
                n_odd += 1
            else:
                n_even += 1
            
            if parity != prev_parity:
                n_change += 1
                prev_parity = parity
        
        answer = max(n_odd, n_even, n_change)
        
        return answer