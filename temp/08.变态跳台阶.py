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
