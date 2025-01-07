class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set) # Key : r
        cols = collections.defaultdict(set) # Key : c
        groups = collections.defaultdict(set) # Key : (r // 3, c // 3)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".": # Continue to pass non-numbers
                    continue
                if board[r][c] in rows[r]: # If exists in row HashSet
                    return False
                if board[r][c] in cols[c]: # If exists in column HashSet
                    return False
                if board[r][c] in groups[(r // 3, c // 3)]: # If exists in 3x3 group HashSet
                    return False
                rows[r].add(board[r][c]) 
                cols[c].add(board[r][c])
                groups[(r // 3, c // 3)].add(board[r][c])
        return True