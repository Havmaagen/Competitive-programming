class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        
        output = num_people * [0]
        i, portion = 0, 1
        while candies:
            if candies <= portion:
                output[i] += candies
                candies = 0
                break
            
            output[i] += portion
            candies -= portion
            portion += 1
            i += 1
            if i == num_people:
                i = 0
        
        return output