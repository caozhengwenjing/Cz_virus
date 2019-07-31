# **题目：**统计一个数字在排序数组中出现的次数。

# -*- coding:utf-8 -*-


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        ans = 0
        for i in range(0, len(data)):
            if data[i] == k:
                ans = ans + 1
            if data[i] > k:
                break
        return ans


if __name__ == '__main__':
    data = [1, 2, 3, 3, 3, 4, 4, 5]
    k = 3
    solution = Solution()
    ans = solution.GetNumberOfK(data, k)
    print(ans)
