class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        
        n = len(s)
        diff_array = (n + 1) * [0]
        for start, end, direction in shifts:
            if direction == 0:
                diff_array[start] -= 1
                diff_array[end + 1] += 1
            else:
                diff_array[start] += 1
                diff_array[end + 1] -= 1
        
        t = n * [0]
        shift = 0
        for i, char in enumerate(s):
            shift += diff_array[i]
            shift %= 26
            j = (ord(char) - ord("a") + shift) % 26 + ord("a")
            t[i] = chr(j)
        
        t = "".join(t)
        
        return t