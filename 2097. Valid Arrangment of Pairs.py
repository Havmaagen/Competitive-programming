class Solution(object):
    def validArrangement(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: List[List[int]]
        """
        
        adj = defaultdict(set)
        in_out_deg_diff = defaultdict(int)
        for u, v in pairs:
            adj[u].add(v)
            in_out_deg_diff[u] -= 1
            in_out_deg_diff[v] += 1
        
        for u in in_out_deg_diff:
            if in_out_deg_diff[u] == -1:
                start = u
                break
        else:
            start = pairs[0][0]
        
        
        Euler_path = []
        stack = [start]
        while stack:
            u = stack[-1]
            if adj[u]:
                stack.append(adj[u].pop())
            else:
                Euler_path.append(stack.pop())
        
        Euler_path.reverse()
        output = [[Euler_path[i - 1], Euler_path[i]] for i in range(1, len(Euler_path))]
        
        return output