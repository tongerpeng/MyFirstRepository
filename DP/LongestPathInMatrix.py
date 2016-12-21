#! /usr/bin/python
# -*- coding: UTF-8 -*-

"""
问题描述：n*n int数组,找这样的路径，路径上的数一次加1,寻找最长的路径
"""

def findLongestFromACell(i, j, mat, dp, n):
    if i < 0 or i >= n or j < 0 or j >= n:
        return 0
    # if the subproblem solved 
    if dp[i][j] != -1:
        return dp[i][j]
    
    if j < n-1 and (mat[i][j] + 1 == mat[i][j+1]):
        dp[i][j] = 1 + findLongestFromACell(i, j+1, mat, dp, n)
        return dp[i][j]
    if j > 0 and (mat[i][j] + 1 == mat[i][j-1]):
        dp[i][j] = 1 + findLongestFromACell(i, j-1, mat, dp, n)
        return dp[i][j]
    if i < n-1 and (mat[i][j] + 1 == mat[i+1][j]):
        dp[i][j] = 1 + findLongestFromACell(i+1, j, mat, dp, n)
        return dp[i][j]
    if i > 0 and (mat[i][j] + 1 == mat[i-1][j]):
        dp[i][j] = 1 + findLongestFromACell(i-1, j, mat, dp, n)
        return dp[i][j]
    dp[i][j] = 1
    return dp[i][j]

def findLongestFromAll(mat, n):
    result = 1
    dp = [[-1] * n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                findLongestFromACell(i, j, mat, dp, n)
                result = max(result, dp[i][j])
    return result


if __name__ == "__main__":
    mat = [[1, 2, 9], [5, 3, 8], [4, 6, 7]]
    print "Length of the longest path is ", findLongestFromAll(mat, 3)
