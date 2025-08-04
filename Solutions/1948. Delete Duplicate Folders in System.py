class Solution(object):
    def deleteDuplicateFolder(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: List[List[str]]
        """
        
        root = TrieNode()
        
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                node = node.children[folder]
        
        
        hashes = defaultdict(int)
        
        def dfs_serialize(node):
            if node.children:
                serial = []
                for folder, child in node.children.items():
                    dfs_serialize(child)
                    serial.append(folder + "(" + child.serial + ")")
                
                node.serial = "".join(sorted(serial))
                hashes[node.serial] += 1
        
        dfs_serialize(root)
        
        
        answer = []
        path = []
        
        def dfs_extract_paths(node):
            if hashes[node.serial] <= 1:
                if path:
                    answer.append(path[:])
                
                for folder, child in node.children.items():
                    path.append(folder)
                    dfs_extract_paths(child)
                    path.pop()
        
        dfs_extract_paths(root)
        
        return answer


class TrieNode():
    def __init__(self):
        self.serial = ""
        self.children = {}