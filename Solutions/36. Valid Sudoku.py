class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        blocks = [[set() for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in rows[i]:
                    return False
                
                if board[i][j] in columns[j]:
                    return False
                
                i0, j0 = i // 3, j // 3
                if board[i][j] in blocks[i0][j0]:
                    return False
                
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                blocks[i0][j0].add(board[i][j])
        
        return True