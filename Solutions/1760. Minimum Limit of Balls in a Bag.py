class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        
        i, j = 1, max(nums)
        while i < j:
            maxSize = (i + j) // 2
            k = 0
            for x in nums:
                k += (x - 1) // maxSize
                if k > maxOperations:
                    i = maxSize + 1
                    break
            else:
                j = maxSize
        
        return i