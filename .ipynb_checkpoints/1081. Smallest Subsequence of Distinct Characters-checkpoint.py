class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        last_occurrence = {x: i for i, x in enumerate(s)}
        
        stack = []
        in_stack = set()
        for i, x in enumerate(s):
            if x not in in_stack:
                while stack and (x < stack[-1]) and (last_occurrence[stack[-1]] > i):
                    in_stack.remove(stack.pop())
                stack.append(x)
                in_stack.add(x)
        
        t = "".join(stack)
        
        return t