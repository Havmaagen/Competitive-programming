class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        n = len(arr)
        for i in range(n - 2, -1, -1):
            if arr[i] == 0:
                arr.pop()
                arr.insert(i, 0)