class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        groups = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r]:
                    return False
                if board[r][c] in cols[c]:
                    return False
                if board[r][c] in groups[(r // 3, c // 3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                groups[(r // 3, c // 3)].add(board[r][c])
        return True