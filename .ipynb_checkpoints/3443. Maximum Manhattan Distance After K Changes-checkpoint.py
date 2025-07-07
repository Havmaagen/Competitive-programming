class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        max_dist = 0
        latitude, longitude = 0, 0
        for i, x in enumerate(s):
            if x == "N":
                latitude += 1
            elif x == "S":
                latitude -= 1
            elif x == "E":
                longitude += 1
            elif x == "W":
                longitude -= 1
            
            max_curr_dist = min(abs(latitude) + abs(longitude) + 2 * k, i + 1)
            max_dist = max(max_dist, max_curr_dist)
        
        return max_dist