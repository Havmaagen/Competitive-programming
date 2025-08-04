class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        answer = list(s)
        stack = [deque() for _ in range(26)]
        for i, char in enumerate(s):
            if char != "*":
                stack[ord(char) - ord("a")].append(i)
            else:
                for j in range(26):
                    if stack[j]:
                        answer[stack[j].pop()] = "*"
                        break
        
        answer = "".join(char for char in answer if char != "*")
        
        return answer