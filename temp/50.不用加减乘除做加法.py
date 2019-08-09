# **题目：**写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
#
# **思路：**二进制异或进位。

# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2!=0:
            sum=num1^num2
            carry=(num1&num2)<<1
            num1=sum
            num2=carry
        return num1

if __name__=='__main__':
    num1,num2=10,500000
    solution=Solution()
    ans=solution.Add(num1,num2)
    print(ans)
