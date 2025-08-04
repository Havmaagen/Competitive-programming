class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        pairs = {"(":")", "[":"]", "{":"}"}
        
        stack = deque()
        for char in s:
            if char in pairs:
                stack.append(pairs[char])
            elif stack and (stack[-1] == char):
                stack.pop()
            else:
                is_valid = False
                break
        else:
            is_valid = not stack
        
        return is_valid