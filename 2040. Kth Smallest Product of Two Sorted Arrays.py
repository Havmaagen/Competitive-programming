class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        
        pos1 = self.find_pos_idx(nums1)
        pos2 = self.find_pos_idx(nums2)
        
        a1, a2 = nums1[0] * nums2[0], nums1[0] * nums2[-1]
        b1, b2 = nums1[-1] * nums2[0], nums1[-1] * nums2[-1]
        min_prod, max_prod = min(a1, a2, b1, b2), max(a1, a2, b1, b2)
        
        left, right = min_prod, max_prod
        while left < right:
            middle = left + (right - left) // 2
            if self.counter(nums1, nums2, pos1, pos2, middle) < k:
                left = middle + 1
            else:
                right = middle
        
        return left
    
    
    def find_pos_idx(self, nums):
        pos = 0
        while (pos < len(nums)) and (nums[pos] < 0):
            pos += 1
        
        return pos
    
    
    def counter(self, nums1, nums2, pos1, pos2, val):
        n1, n2 = len(nums1), len(nums2)
        count = 0
        
        i1, i2 = 0, pos2 - 1
        while (i1 < pos1) and (i2 >= 0):
            if nums1[i1] * nums2[i2] > val:
                i1 += 1
            else:
                count += pos1 - i1
                i2 -= 1
        
        i1, i2 = 0, pos2
        while (i1 < pos1) and (i2 < n2):
            if nums1[i1] * nums2[i2] > val:
                i2 += 1
            else:
                count += n2 - i2
                i1 += 1
        
        i1, i2 = pos1, 0
        while (i1 < n1) and (i2 < pos2):
            if nums1[i1] * nums2[i2] > val:
                i1 += 1
            else:
                count += n1 - i1
                i2 += 1
        
        i1, i2 = pos1, n2 - 1
        while (i1 < n1) and (i2 >= pos2):
            if nums1[i1] * nums2[i2] > val:
                i2 -= 1
            else:
                count += i2 - pos2 + 1
                i1 += 1
        
        return count