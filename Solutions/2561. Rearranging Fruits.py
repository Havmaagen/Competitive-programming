class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        
        freq = defaultdict(int)
        min_cost = float("inf")
        for cost1, cost2 in zip(basket1, basket2):
            freq[cost1] += 1
            freq[cost2] -= 1
            min_cost = min(cost1, cost2, min_cost)
        
        if any(f % 2 for f in freq.values()):
            return -1
        
        swaps = []
        for cost in freq:
            k = abs(freq[cost]) // 2
            swaps.extend(k * [cost])
        
        swaps.sort()
        
        n_swaps = len(swaps) // 2
        min_swap_cost = 2 * min_cost
        answer = sum(min(x, min_swap_cost) for x in swaps[:n_swaps])
        
        return answer