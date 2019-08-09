# **题目：**求1+2+3+…+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
#
# **思路：**利用递归当作计算结果。

# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        if n==0:
            return 0
        return self.Sum_Solution(n-1)+n

if __name__=='__main__':
    n=6
    solution=Solution()
    ans=solution.Sum_Solution(n)
    print(ans)
