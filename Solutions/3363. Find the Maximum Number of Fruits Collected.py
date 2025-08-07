class Solution(object):
    def maxCollectedFruits(self, fruits):
        """
        :type fruits: List[List[int]]
        :rtype: int
        """
        
        n = len(fruits)
        steps = [-1, 0, 1]
        for i in range(1, n - 1):
            j0 = max(i, n - i)
            for j in range(max(i + 1, n - 1 - i), n):
                fruits[i][j] += max(fruits[i - 1][j + s] for s in steps if j0 <= j + s < n)
                fruits[j][i] += max(fruits[j + s][i - 1] for s in steps if j0 <= j + s < n)
        
        answer = sum(fruits[i][i] for i in range(n)) + fruits[n - 2][n - 1] + fruits[n - 1][n - 2]
        
        return answer