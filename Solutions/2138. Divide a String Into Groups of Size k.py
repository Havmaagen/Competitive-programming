class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        
        n = len(s)
        answer = []
        for i in range(0, n, k):
            answer.append(s[i:i+k])
        
        answer[-1] = answer[-1].ljust(k, fill)
        
        return answer