class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        digits = sorted(int(d) for d in str(num))
        answer = (digits[0] + digits[1]) * 10 + (digits[2] + digits[3])
        
        return answer