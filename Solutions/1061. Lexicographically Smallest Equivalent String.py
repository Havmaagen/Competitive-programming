class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        
        dsu = DSU()
        
        for char in string.ascii_lowercase:
            dsu.make(char)
        
        for char1, char2 in zip(s1, s2):
            dsu.union(char1, char2)
        
        minStr = "".join(dsu.find(char) for char in baseStr)
        
        return minStr


class DSU(object):
    def __init__(self):
        self.parent = {}
    
    def make(self, x):
        self.parent[x] = x
    
    def find(self, x):
        while x != self.parent[x]:
            x, self.parent[x] = self.parent[x], self.parent[self.parent[x]]
        return self.parent[x]
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x < y:
            self.parent[y] = x
        elif x > y:
            self.parent[x] = y