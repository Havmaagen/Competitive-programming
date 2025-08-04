# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        if not root:
            return []
        
        max_vals = []
        nodes = [root]
        while nodes:
            val = None
            new_nodes = []
            for node in nodes:
                if (val is None) or (node.val > val):
                    val = node.val
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            max_vals.append(val)
            nodes = new_nodes
        
        return max_vals