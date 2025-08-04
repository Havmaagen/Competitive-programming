class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        
        n = len(nums)
        prefix = (n + 1) * [0]
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        output = float("inf")
        for k in range(l, r + 1):
            for i in range(n - k + 1):
                val = prefix[i + k] - prefix[i]
                if val > 0:
                    output = min(output, val)
        
        return output if (output != float("inf")) else -1