class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        
        s = str(num)
        answer = 0
        unchanged = True
        for char in s:
            if (char == "6") and unchanged:
                answer = 10 * answer + 9
                unchanged = False
            else:
                answer = 10 * answer + int(char)
        
        return answer