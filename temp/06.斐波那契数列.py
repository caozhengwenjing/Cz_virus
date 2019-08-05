# **题目：**大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。n<=39。
#
# **题解：**递归和非递归方法。

# -*- coding:utf-8 -*-


class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        Fib = [0 for i in range(0, n + 1)]
        Fib[0], Fib[1] = 0, 1
        for i in range(2, n + 1):
            Fib[i] = Fib[i - 1] + Fib[i - 2]
        return Fib[n]

    def Fibonacci1(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        else:
            return self.Fibonacci1(n - 1) + self.Fibonacci1(n - 2)


if __name__ == '__main__':
    solution = Solution()
    n = int(input())
    ans = solution.Fibonacci1(n)
    print(ans)
