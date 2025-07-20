class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        
        folder.sort()
        output = [folder[0]]
        for f in folder[1:]:
            if not f.startswith(output[-1] + "/"):
                output.append(f)
        
        return output