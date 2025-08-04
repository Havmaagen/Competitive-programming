class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        result = ""
        for char in s:
            if char == "*":
                if result:
                    result = result[:-1]
            elif char == "#":
                result *= 2
            elif char == "%":
                result = result[::-1]
            else:
                result += char
        
        return result