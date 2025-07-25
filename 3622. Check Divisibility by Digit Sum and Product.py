class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        digit_sum = 0
        digit_product = 1
        tmp = n
        while tmp > 0:
            d = tmp % 10
            digit_sum += d
            digit_product *= d
            tmp /= 10
        
        d = digit_sum + digit_product
        answer = (n % d == 0)
        
        return answer