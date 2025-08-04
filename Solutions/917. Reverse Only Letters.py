class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = list(s)
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            if s[i].isalpha() and s[j].isalpha():
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif (not s[i].isalpha()) and (not s[j].isalpha()):
                i += 1
                j -= 1
            elif not s[i].isalpha():
                i += 1
            else:
                j -= 1
        
        s = "".join(s)
        
        return s