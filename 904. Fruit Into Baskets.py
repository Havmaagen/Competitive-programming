class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        answer = 0
        fruit1, fruit2 = -1, -1
        total, current = 0, 0
        for fruit in fruits:
            if fruit == fruit2:
                total += 1
                current += 1
            elif fruit == fruit1:
                total += 1
                current = 1
                fruit1, fruit2 = fruit2, fruit1
            else:
                total = current + 1
                current = 1
                fruit1, fruit2 = fruit2, fruit
            
            answer = max(total, answer)
        
        return answer