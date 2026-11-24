
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        low, high = 0, rows - 1

        while low < high:
            mid = low + (high - low) // 2

            # column of the max element in the middle row
            best_col = max(range(cols), key=lambda c: mat[mid][c])

            if mat[mid][best_col] > mat[mid + 1][best_col]:
                high = mid        # a peak exists in this row or above
            else:
                low = mid + 1     # a peak exists in the rows below

        best_col = max(range(cols), key=lambda c: mat[low][c])
        return [low, best_col]


