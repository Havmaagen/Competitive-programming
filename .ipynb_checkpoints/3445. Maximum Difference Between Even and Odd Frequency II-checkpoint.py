class Solution(object):
    def maxDifference(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        n = len(s)
        answer = -n
        for a, b in product("01234", repeat=2):
            if a == b:
                continue
            
            min_diff = 4 * [n]
            left = -1
            left_a, left_b, right_a, right_b = 0, 0, 0, 0
            for right in range(n):
                if s[right] == a:
                    right_a += 1
                elif s[right] == b:
                    right_b += 1
                
                while (right - left >= k) and (right_b - left_b >= 2):
                    left_status = 2 * (left_a & 1) + (left_b & 1)
                    min_diff[left_status] = min(min_diff[left_status], left_a - left_b)
                    
                    left += 1
                    if s[left] == a:
                        left_a += 1
                    elif s[left] == b:
                        left_b += 1
                
                right_status = 2 * (right_a & 1) + (right_b & 1)
                status = right_status ^ 2
                answer = max(answer, (right_a - right_b) - min_diff[status])
        
        return answer