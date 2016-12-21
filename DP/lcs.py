#! /usr/bin/python
# -*- coding:UTF-8 -*-

def lcsRecursion(X, Y, m, n):
    
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcsRecursion(X, Y, m-1, n-1)
    else:
        return max(lcsRecursion(X, Y, m, n-1), lcsRecursion(X, Y, m-1, n))

def lcs(X, Y):

    m = len(X)
    n = len(Y)
    dp = [[0] * (n+1) for i in xrange(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
 
if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print "Length of LCS is ", lcsRecursion(X, Y, len(X), len(Y))
    print "Length of LCS is ", lcs(X, Y)
