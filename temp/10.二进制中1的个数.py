# **题目：**输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
#
# **题解：**每次进行左移一位，然后与1进行相与，如果是1则进行加1。

# -*- coding:utf-8 -*-


class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        for i in range(32):
            count += (n >> i) & 1
        return count


if __name__ == '__main__':
    solution = Solution()
    n = int(input())
    ans = solution.NumberOf1(n)
    print(ans)
