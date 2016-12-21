#! /usr/bin/python
# -*- coding: UTF-8 -*-

"""
问题描述：
    对于两个字符串，可以替换，删除，增加任意字符使得两个字符串一样，每一次操作都算一步
求使得两个字符串相同的最小步数。
"""
import time

def editDistanceRecursion(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return editDistanceRecursion(str1, str2, m-1, n-1)

    return 1 + min(editDistanceRecursion(str1, str2, m, n-1),        #Insert
                   editDistanceRecursion(str1, str2, m-1, n-1),      #Replace
                   editDistanceRecursion(str1, str2, m-1, n)         #Add
                  )


def editDistanceDP(str1, str2, m, n):
    dp = [[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],                       #Insert
                                   dp[i-1][j-1],                     #Replace
                                   dp[i-1][j]                        #Add
                                  )
    return dp[m][n]

if __name__ == "__main__":
    str1 = "sundaysdf"
    str2 = "saturday"
    begin = time.time()
    print "use Recursion function: ", editDistanceRecursion(str1, str2, len(str1), len(str2))
    print "costs time: %d ms" % (time.time() - begin)
    begin = time.time()
    print "use DP function: ", editDistanceDP(str1, str2, len(str1), len(str2))
    print "costs time: %d ms" % (time.time() -begin)
