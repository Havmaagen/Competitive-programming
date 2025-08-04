class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        counter = defaultdict(int)
        for x in s:
            counter[x] += 1
        
        elements = sorted(counter.keys(), key=lambda x: counter[x], reverse=True)
        output = "".join(counter[x] * x for x in elements)
        
        return output