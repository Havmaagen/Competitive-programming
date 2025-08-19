class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        
        answer = ""
        digit = ""
        count = 0
        for char in chain(num, "*"):
            if char == digit:
                count += 1
            else:
                if (count >= 3) and (digit > answer):
                    answer = 3 * digit
                
                digit = char
                count = 1
        
        return answer