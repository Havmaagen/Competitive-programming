class Solution(object):
    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        """
        :type n: int
        :type firstPlayer: int
        :type secondPlayer: int
        :rtype: List[int]
        """
        
        self.min_val = n
        self.max_val = 0
        
        def dfs(left, mid, right, count):
            if left == right:
                self.min_val = min(self.min_val, count)
                self.max_val = max(self.max_val, count)
            else:
                n_players = left + mid + right + 2
                half = n_players // 2
                n_players = (n_players + 1) // 2
                count += 1
                if (left + 1 <= half) and (right + 1 <= half):
                    if left < right:
                        for i in range(left + 1):
                            for j in range(left - i, right - i):
                                k = n_players - (i + j + 2)
                                dfs(i, k, j, count)
                    else:
                        for j in range(right + 1):
                            for i in range(right - j, left - j):
                                k = n_players - (i + j + 2)
                                dfs(i, k, j, count)
                elif right + 1 > half:
                    for i in range(left + 1):
                        for k in range(mid + 1):
                            j = n_players - (i + k + 2)
                            dfs(i, k, j, count)
                else:
                    for j in range(right + 1):
                        for k in range(mid + 1):
                            i = n_players - (j + k + 2)
                            dfs(i, k, j, count)
        
        left = firstPlayer - 1
        mid = secondPlayer - firstPlayer - 1
        right = n - secondPlayer
        
        dfs(left, mid, right, 1)
        
        answer = [self.min_val, self.max_val]
        
        return answer