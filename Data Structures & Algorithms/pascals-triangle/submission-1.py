class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        
        rows = [[1]]
        for i in range(numRows-1):
            row = rows[i]
            tmp = [0] + row + [0]
            next_row = []
            for j in range(len(tmp) - 1):
                next_row.append(sum(tmp[j:j+2]))
            rows.append(next_row)
        return rows
            