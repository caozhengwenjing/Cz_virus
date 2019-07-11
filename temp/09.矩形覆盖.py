# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        Fib = [0 for i in range(0, number + 1)]
        Fib[1], Fib[2] = 1, 2
        for i in range(3, number + 1):
            Fib[i] = Fib[i - 1] + Fib[i - 2]
        return Fib[number]


if __name__ == '__main__':
    solution = Solution()
    n = int(input())
    ans = solution.rectCover(n)
    print(ans)
