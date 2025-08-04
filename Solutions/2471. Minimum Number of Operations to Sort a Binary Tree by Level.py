# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        output = 0
        nodes = [root]
        while nodes:
            val_idx, new_nodes = [], []
            for i, node in enumerate(nodes):
                val_idx.append((node.val, i))
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            
            val_idx.sort()
            n, i = len(val_idx), 0
            while i < n:
                j = val_idx[i][1]
                if i != j:
                    val_idx[i], val_idx[j] = val_idx[j], val_idx[i]
                    output += 1
                    i -= 1
                i += 1
            
            nodes = new_nodes
        
        return output