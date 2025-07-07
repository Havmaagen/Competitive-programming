class Solution(object):
    def longestSubsequenceRepeatedK(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        
        candidates = sorted((char for char, f in freq.items() if f >= k), reverse=True)
        
        answer = ""
        queue = deque(candidates)
        while queue:
            t1 = queue.popleft()
            
            if len(t1) > len(answer):
                answer = t1
            
            for char in candidates:
                t2 = t1 + char
                s_it = iter(s)
                if all(char in s_it for char in k * t2):
                    queue.append(t2)
        
        return answer