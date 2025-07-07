class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        
        m, n = len(board), len(board[0])
        neighbours = [set() for _ in range(m * n)]
        for k in range(m * n):
            for e in {-1, 1}:
                i, j = k // (m + 1), k % (m + 1)
                p, q = i + e, j + e
                if 0 <= p < m:
                    neighbours[k].add(p * (m + 1) + j)
                if 0 <= q < n:
                    neighbours[k].add(i * (m + 1) + q)
        
        
        board0 = tuple(range(1, m * n)) + (0,)
        state = board0
        d = {state: 0}
        states = {state}
        moves = 0
        while states:
            moves += 1
            new_states = set()
            for state in states:
                new_state = list(state)
                i = new_state.index(0)
                for j in neighbours[i]:
                    new_state[i], new_state[j] = new_state[j], new_state[i]
                    s = tuple(new_state)
                    if s not in d:
                        d[s] = moves
                        new_states.add(s)
                    new_state[i], new_state[j] = new_state[j], new_state[i]
            
            states = new_states
        
        
        board = tuple(s for row in board for s in row)
        output = d[board] if (board in d) else -1
        
        return output