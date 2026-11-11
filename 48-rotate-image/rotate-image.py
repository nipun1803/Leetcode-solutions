class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        e_l = len(matrix)
        top = 0
        bott = e_l-1
        while top<bott:
            for c in range(e_l):
                temp = matrix[top][c]
                matrix[top][c] = matrix[bott][c]
                matrix[bott][c] = temp
            top+=1
            bott-=1
        for r in range(e_l):
            for c in range(r+1,e_l):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp

        return matrix