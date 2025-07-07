class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        
        n = len(nums)
        if (p == 0) or (n < 2 * p):
            return 0
        
        nums.sort()
        left, right = 0, nums[n - 1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            count, i = 0, 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1
            
            if count < p:
                left = mid + 1
            else:
                right = mid
        
        return left