# **题目：**请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
#             例如，字符串"+100",“5e2”,"-123",“3.1416"和”-1E-16"都表示数值。
#             但是"12e",“1a3.14”,“1.2.3”,"±5"和"12e+4.3"都不是


# -*- coding:utf-8 -*-


class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        # 标记符号、小数点、e是否出现过
        sign, decimal, hasE = False, False, False
        for i in range(0, len(s)):
            if s[i] == 'e' or s[i] == 'E':
                if i == len(s) - 1:  # e后面一定要接数字
                    return False
                if hasE == True:  # 不能出现两次e
                    return False
                hasE = True
            elif s[i] == '+' or s[i] == '-':
                # 第二次出现+或-一定要在e之后
                if sign and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
                # 第一次出现+或-，如果不是出现在字符最前面，那么就要出现在e或者E后面
                if sign == False and i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
                sign = True
            elif s[i] == '.':
                # e后面不能出现小数点，小数点不能出现两次
                if decimal or hasE:
                    return False
                decimal = True
            elif s[i] > '9' or s[i] < '0':
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    s = '123e.1416'
    ans = solution.isNumeric(s)
    print(ans)
