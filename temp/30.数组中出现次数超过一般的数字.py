# **题目：**数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
#         例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
#         超过数组长度的一半，因此输出2。如果不存在则输出0
#
# **题解：**利用list列表来存放每个数出现的次数ans[numbers[i]]=ans[numbers[i]]+1。

# -*- coding:utf-8 -*-


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        numlen = len(numbers)
        halflen = numlen // 2
        maxans = 0
        ans = [0 for i in range(0, 1000)]
        for i in range(0, len(numbers)):
            ans[numbers[i]] = ans[numbers[i]] + 1
            if ans[numbers[i]] > maxans:
                maxans = numbers[i]
        ans.sort()
        ans.reverse()
        res = ans[0]
        if res > halflen:
            return maxans
        else:
            return 0


if __name__ == '__main__':
    num = list(map(int, input().split(',')))
    solution = Solution()
    ans = solution.MoreThanHalfNum_Solution(num)
    print(ans)
