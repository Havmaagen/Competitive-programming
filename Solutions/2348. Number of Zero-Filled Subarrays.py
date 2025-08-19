class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        answer = 0
        count = 0
        for num in chain(nums, ["*"]):
            if num == 0:
                count += 1
            else:
                answer += count * (count + 1) / 2
                count = 0
        
        return answer