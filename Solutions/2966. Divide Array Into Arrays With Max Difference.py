class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        nums.sort()
        
        n = len(nums)
        answer = []
        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] <= k:
                answer.append(nums[i:i+3])
            else:
                answer = []
                break
        
        return answer