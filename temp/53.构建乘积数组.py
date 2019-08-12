# 题目
# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
# 其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

# 思路
# 审题仔细 没有A[i]

# -*- coding:utf-8 -*-


class Solution:
    def multiply(self, A):
        # write code here
        B = []
        for i in range(0, len(A)):
            temp = 1
            for j in range(0, len(A)):
                if j == i:
                    continue
                temp = temp * A[j]
            B.append(temp)
        return B


if __name__ == '__main__':
    solution = Solution()
    A = [1, 2, 3, 4, 5]
    ans = solution.multiply(A)
    print(ans)
