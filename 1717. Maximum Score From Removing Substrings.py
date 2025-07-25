class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        
        char1, char2 = "a", "b"
        if x < y:
            char1, char2 = char2, char1
            x, y = y, x
        
        score = 0
        count1, count2 = 0, 0
        for char in itertools.chain(s, "*"):
            if char == char1:
                count1 += 1
            elif char == char2:
                if count1 > 0:
                    score += x
                    count1 -= 1
                else:
                    count2 += 1
            else:
                score += min(count1, count2) * y
                count1, count2 = 0, 0
        
        return score