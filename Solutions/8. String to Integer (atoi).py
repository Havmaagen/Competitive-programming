class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        answer = 0
        sign = 0
        special = {" ":0, "-":-1, "+":1}
        for char in s:
            if char in special:
                if sign == 0:
                    sign = special[char]
                    continue
                else:
                    break
            
            if char.isdigit():
                if sign == 0:
                    sign = 1
                answer = 10 * answer + int(char)
            else:
                break
        
        answer = min(max(sign * answer, -(2**31)), 2**31 - 1)
        
        return answer