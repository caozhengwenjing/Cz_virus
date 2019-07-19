# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
# 例如，如果输入如下矩阵：
#  1 2 3 4
#  5 6 7 8
#  9 10 11 12
#  13 14 15 16
# 则依次打印出数字
# 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

# **思路：**每次打印圈，但要判断最后一次是打印横还是竖，另外判断数据是否已存在。
# -*- coding:utf-8 -*-


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        m, n = len(matrix), len(matrix[0])
        res = []
        if n == 1 and m == 1:
            res.append(matrix[0][0])
            return res
        for k in range(0, (min(m, n) + 1) // 2):
            [res.append(matrix[k][i]) for i in range(k, n - k)]
            [res.append(matrix[j][n - k - 1]) for j in range(k, m - k) if matrix[j][n - k - 1] not in res]
            [res.append(matrix[m - k - 1][j]) for j in range(n - k - 1, k - 1, -1) if matrix[m - k - 1][j] not in res]
            [res.append(matrix[j][k]) for j in range(m - 1 - k, k - 1, -1) if matrix[j][k] not in res]
        return res


if __name__ == '__main__':
    solution = Solution()
    m, n = 1, 5
    matrix = []
    for i in range(0, m):
        matrix.append(list(map(int, input().split(' '))))
    print(matrix)
    ans = solution.printMatrix(matrix)
    print(ans)
