# -*- coding:utf-8 -*-


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        minnum = 999999
        for i in range(0, len(rotateArray)):
            if minnum > rotateArray[i]:
                minnum = rotateArray[i]
        if minnum:
            return minnum
        else:
            return 0


if __name__ == '__main__':
    solution = Solution()
    rotateArray = list(map(int, input().split(',')))
    ans = solution.minNumberInRotateArray(rotateArray)
    print(ans)
