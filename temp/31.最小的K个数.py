# **题目：**输入n个整数，找出其中最小的K个数，例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        tinput.sort()
        return tinput[:k]


if __name__ == '__main__':
    num = list(map(int, input().split(',')))
    k = int(input())
    solution = Solution()
    ans = solution.GetLeastNumbers_Solution(num, k)
    print(ans)
