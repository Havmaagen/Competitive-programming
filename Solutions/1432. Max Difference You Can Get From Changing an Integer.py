class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        s = str(num)
        answer = 0
        d_max, d_min, val_min = None, None, 0
        for i, d in enumerate(s):
            if (d_max is None) and (d != "9"):
                d_max = d
            if (d_min is None) and (d not in {"0", "1"}):
                d_min = d
                val_min = 1 if (i == 0) else 0
            
            x = 9 if (d == d_max) else int(d)
            y = val_min if (d == d_min) else int(d)
            answer = 10 * answer + (x - y)
        
        return answer