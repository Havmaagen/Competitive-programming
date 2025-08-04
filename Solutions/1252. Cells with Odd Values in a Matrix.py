class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        
        dr, dc = defaultdict(int), defaultdict(int)
        for i, j in indices:
            dr[i] += 1
            dc[j] += 1
        
        n_odd_nums = 0
        for i in range(m):
            for j in range(n):
                if (dr[i] + dc[j]) % 2 == 1:
                    n_odd_nums += 1
        
        return n_odd_nums