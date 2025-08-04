class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        A1, A2 = -2147483648, 2147483647
        d1 = A1 % 10
        d1 = -(10 - d1) if (d1 > 0) else d1
        a1 = (A1 - d1) / 10
        a2, d2 = divmod(A2, 10)
        
        output = 0
        
        while x < 0:
            d = x % 10
            d = -(10 - d) if (d > 0) else d
            x = (x - d) / 10
            if (output < a1) or ((output == a1) and (d < d1)):
                return 0
            output = 10 * output + d
        
        while x > 0:
            x, d = divmod(x, 10)
            if (output > a2) or ((output == a2) and (d > d2)):
                return 0
            output = 10 * output + d
        
        return output