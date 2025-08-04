class Solution(object):
    def minimumScore(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        enter_time = n * [0]
        exit_time = n * [0]
        subtree_xors = n * [0]
        
        def dfs(u, parent, timer):
            enter_time[u] = timer
            timer += 1
            
            subtree_xors[u] = nums[u]
            for v in adj[u]:
                if v == parent:
                    continue
                
                timer = dfs(v, u, timer)
                subtree_xors[u] ^= subtree_xors[v]
                exit_time[u] = timer
            
            return timer
        
        dfs(0, -1, 0)
        
        answer = float("inf")
        for u in range(1, n):
            for v in range(u + 1, n):
                if enter_time[u] < enter_time[v] < exit_time[u]:
                    xor1 = subtree_xors[0] ^ subtree_xors[u]
                    xor2 = subtree_xors[u] ^ subtree_xors[v]
                    xor3 = subtree_xors[v]
                elif enter_time[v] < enter_time[u] < exit_time[v]:
                    xor1 = subtree_xors[0] ^ subtree_xors[v]
                    xor2 = subtree_xors[v] ^ subtree_xors[u]
                    xor3 = subtree_xors[u]
                else:
                    xor1 = subtree_xors[0] ^ subtree_xors[u] ^ subtree_xors[v]
                    xor2 = subtree_xors[u]
                    xor3 = subtree_xors[v]
                
                max_xor, min_xor = max(xor1, xor2, xor3), min(xor1, xor2, xor3)
                answer = min(max_xor - min_xor, answer)
        
        return answer