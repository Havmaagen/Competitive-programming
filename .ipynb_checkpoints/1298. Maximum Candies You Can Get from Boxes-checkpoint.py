class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        
        open_boxes, closed_boxes = set(), set()
        for i in initialBoxes:
            if status[i] == 1:
                open_boxes.add(i)
            else:
                closed_boxes.add(i)
        
        n_candies = 0
        while open_boxes:
            i = open_boxes.pop()
            n_candies += candies[i]
            candies[i] = 0
            
            for j in keys[i]:
                if candies[j] > 0:
                    status[j] = 1
                    if j in closed_boxes:
                        closed_boxes.remove(j)
                        open_boxes.add(j)
            
            for j in containedBoxes[i]:
                if candies[j] > 0:
                    if status[j] == 1:
                        open_boxes.add(j)
                    else:
                        closed_boxes.add(j)
        
        return n_candies