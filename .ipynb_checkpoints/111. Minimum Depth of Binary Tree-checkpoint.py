# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        if not root:
            return 0
        
        min_depth = 1
        nodes = [root]
        while nodes:
            new_nodes = []
            for node in nodes:
                if not node.left and not node.right:
                    return min_depth
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            
            nodes = new_nodes
            min_depth += 1
        
        return min_depth