class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        diff01 = 0
        swaps0, swaps1 = 0, 0
        w0, w1 = 0, 0
        for i, num in enumerate(nums):
            if num & 1 == 0:
                diff01 += 1
                swaps0 += abs(i - w0)
                w0 += 2
            else:
                diff01 -= 1
                swaps1 += abs(i - w1)
                w1 += 2
        
        if diff01 == 1:
            swaps = swaps0
        elif diff01 == 0:
            swaps = min(swaps0, swaps1)
        elif diff01 == -1:
            swaps = swaps1
        else:
            swaps = -1
        
        return swaps