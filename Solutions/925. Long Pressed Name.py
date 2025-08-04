class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        
        m, n = len(name), len(typed)
        i, j = 0, 0
        while (i < m) and (j < n):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0:
                if typed[j] == typed[j - 1]:
                    j += 1
                else:
                    return False
            else:
                return False
        
        if (i < m) and (j == n):
            return False
        elif (i == m) and (j < n):
            return all(typed[k] == typed[j - 1] for k in range(j, n))
        else:
            return True