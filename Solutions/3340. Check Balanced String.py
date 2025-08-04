class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        return (sum(s if (i & 1 == 0) else -s for i, s in enumerate(map(int, num))) == 0)