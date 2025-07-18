class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        
        n = len(pattern)
        answer = []
        stack = []
        for i in range(n + 1):
            stack.append(str(i + 1))
            if (i == n) or (pattern[i] == "I"):
                while stack:
                    answer.append(stack.pop())
        
        answer = "".join(answer)
        
        return answer