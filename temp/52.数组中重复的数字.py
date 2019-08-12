# **题目：**在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
#             也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
#             例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
#
# **思路：**利用dict计算重复数字。

# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        numset = set(numbers)
        dict = {}
        duplication.append(0)
        for val in numbers:
            dict[val] = 0
        for i in range(0, len(numbers)):
            dict[numbers[i]] = dict[numbers[i]] + 1
        for val in numset:
            if dict[val] > 1:
                duplication[0] = val
                return True
        return False


if __name__ == '__main__':
    numbers = [2, 1, 1, 2, 4]
    solution = Solution()
    duplication = []
    ans = solution.duplicate(numbers, duplication)
    print(ans)
