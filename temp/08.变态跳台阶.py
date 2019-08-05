# **题目：**一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
#
# **题解：**ans[n]=ans[n-1]+ans[n-2]+ans[n-3]+…+ans[n-n]，ans[n-1]=ans[n-2]+ans[n-3]+…+ans[n-n]，ans[n]=2*ans[n-1]。

# -*- coding:utf-8 -*-


class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        return 2 * self.jumpFloorII(number - 1)


if __name__ == '__main__':
    solution = Solution()
    n = int(input())
    ans = solution.jumpFloorII(n)
    print(ans)
