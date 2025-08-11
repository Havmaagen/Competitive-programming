class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        s = bin(n)[-1:1:-1]
        prefix = [0]
        for i, char in enumerate(s):
            if char == "1":
                prefix.append(prefix[-1] + i)
        
        MOD = 10**9 + 7
        answer = [pow(2, prefix[r + 1] - prefix[l], MOD) for l, r in queries]
        
        return answer