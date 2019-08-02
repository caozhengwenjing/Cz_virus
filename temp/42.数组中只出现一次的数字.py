# **题目：**一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。
#
# **题解：**将数组中数转到set之中，然后利用dict存储每个数字出现的次数。
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        arrayset = set(array)
        dict = {}
        for num in arrayset:
            dict[num] = 0
        for i in range(0, len(array)):
            dict[array[i]] = dict[array[i]] + 1
        ans = []
        for num in arrayset:
            if dict[num] == 1:
                ans.append(num)
        return ans


if __name__ == '__main__':
    array = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 7, 9]
    solution = Solution()
    ans = solution.FindNumsAppearOnce(array)
    print(ans)
