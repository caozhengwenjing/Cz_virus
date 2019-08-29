# **题目：**地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
#   每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
#   例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），
#   因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
#
# **思路：**对未走过的路径进行遍历，搜索所有的路径值。
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.vis = {}

    def movingCount(self, threshold, rows, cols):
        # write code here
        return self.moving(threshold, rows, cols, 0, 0)

    def moving(self, threshold, rows, cols, row, col):
        rowans, colans = 0, 0
        rowtemp, coltemp = row, col
        while rowtemp > 0:
            rowans = rowans + rowtemp % 10
            rowtemp = rowtemp // 10
        while coltemp > 0:
            colans = colans + coltemp % 10
            coltemp = coltemp // 10

        if rowans + colans > threshold:
            return 0
        if row >= rows or col >= cols or row < 0 or col < 0:
            return 0
        if (row, col) in self.vis:
            return 0
        self.vis[(row, col)] = 1

        return 1 + self.moving(threshold, rows, cols, row - 1, col) + \
               self.moving(threshold, rows, cols, row + 1, col) + \
               self.moving(threshold, rows, cols, row, col - 1) + \
               self.moving(threshold, rows, cols, row, col + 1)


if __name__ == '__main__':
    solution = Solution()
    threshold = 10
    rows, cols = 1, 100
    ans = solution.movingCount(threshold, rows, cols)
    print(ans)
