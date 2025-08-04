class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        
        arr.sort()
        n = len(arr)
        pairs = []
        min_abs_diff = arr[1] - arr[0]
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min_abs_diff:
                min_abs_diff = diff
                pairs = [[arr[i], arr[i + 1]]]
            elif diff == min_abs_diff:
                pairs.append([arr[i], arr[i + 1]])
        
        return pairs