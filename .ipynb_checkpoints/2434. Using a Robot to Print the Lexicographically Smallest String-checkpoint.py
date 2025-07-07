class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)
        suffix = n * [0]
        min_char, counter, idx = s[-1], 1, n - 1
        suffix[-1] = (min_char, counter, idx)
        for i in range(n - 2, -1, -1):
            if s[i] == min_char:
                counter += 1
            elif s[i] < min_char:
                min_char, counter, idx = s[i], 1, i
            suffix[i] = (min_char, counter, idx)
        
        t, answer = deque(), deque()
        i = 0
        while i < n:
            min_char, counter, idx = suffix[i]
            
            while t and (t[-1] <= min_char):
                answer.append(t.pop())
            
            t.extend(s[j] for j in range(i, idx) if s[j] != min_char)
            answer.extend(min_char for _ in range(counter))
            i = idx + 1
        
        if t:
            t.reverse()
            answer.extend(t)
        
        answer = "".join(answer)
        
        return answer