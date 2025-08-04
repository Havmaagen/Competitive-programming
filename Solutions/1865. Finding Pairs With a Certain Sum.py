class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        
        self.nums1 = nums1
        self.nums2 = nums2
        
        self.freq1 = defaultdict(int)
        for num in nums1:
            self.freq1[num] += 1
        
        self.freq2 = defaultdict(int)
        for num in nums2:
            self.freq2[num] += 1
    
    
    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        
        num = self.nums2[index]
        if num in self.freq2:
            self.freq2[num] -= 1
            if self.freq2[num] == 0:
                self.freq2.pop(num)
        
        self.nums2[index] += val
        self.freq2[num + val] += 1
    
    
    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        
        count = 0
        for num in self.freq1:
            if (tot - num) in self.freq2:
                count += self.freq1[num] * self.freq2[tot - num]
        
        return count



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)