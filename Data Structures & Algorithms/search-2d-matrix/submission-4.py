class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
# 6 + 1 = 7
# 7 // 4 = 1 = col
# 7 - 1*4 = 3 = row
        def index_to_cordinate(index, len_row, len_col) -> tuple[int, int]:
            col = index // len_row 
            row = index - (col*len_row)
            return (row, col)

        len_row = len(matrix[0])
        len_col = len(matrix)

        r = len_row*len_col -1
        l = 0

        while l <= r:
            mid = (l + r) // 2
            (row, col) = index_to_cordinate(mid, len_row, len_col)
            value = matrix[col][row]
            if value < target:
                l = mid + 1
            elif value > target:
                r = mid - 1
            elif value == target:
                return True

        return False
