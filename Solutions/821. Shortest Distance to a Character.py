class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        
        n = len(s)
        answer = n * [n]
        prev, nxt = -n, 2 * n
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], abs(i - prev))
            
            j = n - 1 - i
            if s[j] == c:
                nxt = j
            answer[j] = min(answer[j], abs(j - nxt))
        
        return answer