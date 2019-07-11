# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        ans = 1
        for i in range(0, abs(exponent)):
            ans = ans * base
        if exponent > 0:
            return ans
        else:
            return 1 / ans


if __name__ == '__main__':
    solution = Solution()
    base = float(input())
    exponent = int(input())
    ans = solution.Power(base, exponent)
    print(ans)
