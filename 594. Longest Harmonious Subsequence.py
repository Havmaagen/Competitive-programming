class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        answer = 0
        for num in freq:
            if num + 1 in freq:
                answer = max(freq[num] + freq[num + 1], answer)
        
        return answer