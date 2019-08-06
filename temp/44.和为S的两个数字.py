# **题目：**输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
#                             如果有多对数字的和等于S，输出两个数的乘积最小的。
#
# **输出描述：**对应每个测试案例，输出两个数，小的先输出。
#
# **思路：**利用i和j从后面进行扫描结果，选取最小的乘积放入到结果集之中。
# -*- coding:utf-8 -*-


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        ans = []
        i, j, minres = 0, len(array) - 1, 1000000
        for i in range(0, len(array) - 1):
            j = len(array) - 1
            while True:
                tempsum = array[i] + array[j]
                if tempsum == tsum:
                    if array[i] * array[j] < minres:
                        ans = []
                        ans.append(array[i])
                        ans.append(array[j])
                        minres = array[i] * array[j]
                    break
                else:
                    j = j - 1
                if tempsum < tsum:
                    break
                if j <= i:
                    break
        return ans


if __name__ == '__main__':
    array = [1, 2, 4, 7, 11, 15]
    tsum = 15
    solution = Solution()
    ans = solution.FindNumbersWithSum(array, tsum)
    print(ans)
