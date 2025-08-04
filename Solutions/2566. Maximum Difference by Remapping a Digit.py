class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        s = str(num)
        answer = 0
        d_max, d_min = None, s[0]
        for d in s:
            if (d_max is None) and (d != "9"):
                d_max = d
            x = 9 if (d == d_max) else int(d)
            y = 0 if (d == d_min) else int(d)
            answer = 10 * answer + (x - y)
        
        return answer