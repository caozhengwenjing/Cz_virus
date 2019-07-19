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
