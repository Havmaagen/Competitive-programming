class Solution(object):
    def calculateScore(self, instructions, values):
        """
        :type instructions: List[str]
        :type values: List[int]
        :rtype: int
        """
        
        n = len(instructions)
        i, score = 0, 0
        while (i >= 0) and (i < n):
            if instructions[i] == "add":
                instructions[i] = ""
                score += values[i]
                i += 1
            elif instructions[i] == "jump":
                instructions[i] = ""
                i += values[i]
            else:
                break
        
        return score