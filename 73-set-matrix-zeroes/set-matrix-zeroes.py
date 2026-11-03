class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        f_c = False
        f_r = False
        # 1st col
        for i in range(m):
            if matrix[i][0] == 0:
                f_c = True

        # 1st row
        for j in range(n):
            if matrix[0][j] == 0:
                f_r = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if f_r:
            for j in range(n):
                matrix[0][j] = 0

        if f_c:
            for i in range(m):
                matrix[i][0] = 0