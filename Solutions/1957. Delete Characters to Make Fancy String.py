class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        chars = []
        prev_char = None
        count = 0
        for char in s:
            if char == prev_char:
                if count < 2:
                    count += 1
                    chars.append(char)
            else:
                prev_char = char
                count = 1
                chars.append(char)
        
        answer = "".join(chars)
        
        return answer