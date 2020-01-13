# **题目：**一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
#
# **题解：**ans[n]=ans[n-1]+ans[n-2]


class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        ans = [0 for i in range(0, number + 1)]
        ans[1], ans[2] = 1, 2
        for i in range(3, number + 1):
            ans[i] = ans[i - 1] + ans[i - 2]
        return ans[number]


if __name__ == '__main__':
    solution = Solution()
    n = int(input())
    ans = solution.jumpFloor(n)
    print(ans)
