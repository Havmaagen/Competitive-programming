class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        answer = []
        x = 1
        while len(answer) < n:
            if x <= n:
                answer.append(x)
                x *= 10
            else:
                x /= 10
                while x % 10 == 9:
                    x /= 10
                x += 1
        
        return answer