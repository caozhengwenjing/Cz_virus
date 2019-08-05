# **题目：**我们可以用21的小矩形横着或者竖着去覆盖更大的矩形。请问用n个21的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
#
# **题解：**新增加的小矩阵竖着放，则方法与n-1时相同，新增加的小矩阵横着放，则方法与n-2时相同，于是f(n)=f(n-1)+f(n-2)。

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
