class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        answer = 1
        k -= 1
        while k > 0:
            steps = self.counter(n, answer)
            if steps <= k:
                answer += 1
                k -= steps
            else:
                answer *= 10
                k -= 1
        
        return answer
    
    
    def counter(self, n, node):
        steps = 0
        start, end = node, node + 1
        while start <= n:
            steps += min(n + 1, end) - start
            start *= 10
            end *= 10
        
        return steps