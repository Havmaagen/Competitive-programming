class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        
        answer = 0
        count = 0
        left = 1
        while count < n:
            right = 10 * left
            for use_last_digit in [False, True]:
                num = left
                while (num < right) and (count < n):
                    palindrome = self.make_palindrome(num, use_last_digit)
                    if self.is_k_mirror(k, palindrome):
                        answer += palindrome
                        count += 1
                    num += 1
            
            left = right
        
        return answer
    
    
    def make_palindrome(self, num, use_last_digit):
        palindrome = num
        if not use_last_digit:
            num //= 10
        while num:
            palindrome = 10 * palindrome + num % 10
            num //= 10
        
        return palindrome
    
    
    def is_k_mirror(self, k, num):
        s = []
        while num:
            s.append(num % k)
            num //= k
        
        d = len(s)
        val = all(s[i] == s[-(i + 1)] for i in range(d // 2))
        
        return val