# **题目：**输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
#
# **思路：**将数组转换成字符串之后，进行两两比较字符串的大小，比如3,32的大小由332和323确定，即3+32和32+3确定。


# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        num = map(str, numbers)
        for i in range(0, len(numbers)):
            for j in range(i, len(numbers)):
                if int(str(numbers[i]) + str(numbers[j])) > int(str(numbers[j]) + str(numbers[i])):
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        ans = ''
        for i in range(0, len(numbers)):
            ans = ans + str(numbers[i])
        return ans


if __name__ == '__main__':
    numbers = [3, 32, 321]
    solution = Solution()
    ans = solution.PrintMinNumber(numbers)
    print(ans)
