#! /usr/bin/python
# -*- coding: UTF-8 -*-

"""
问题描述：给一个数组，一个目标值，判断数组中是否存在和为目标值的子数组
"""

def hasSubSetSumRecursion(num, n, target):
    '''递归方法'''
    if target == 0:
        return True
    if n == 0 and target != 0:
        return False
    if num[n-1] > target:
        return hasSubSetSumRecursion(num, n-1, target)
    
    return hasSubSetSumRecursion(num, n-1, target) or \
               hasSubSetSumRecursion(num, n-1, target - num[n-1])


def hasSubSetSumDP(num, n, target):
    '''DP方法.'''
    dp = [[False] * (n +1) for i in range(target+1)]

    for i in range(n+1):
        dp[0][i] = True

    for i in range(target):
        dp[i][0] = False
    
    for i in range(1, target+1):
        for j in range(1, n+1):
              dp[i][j] = dp[i][j-1]
              if i >= num[j-1]:
                  dp[i][j] = dp[i][j] or dp[i - num[j-1]][j-1]  # j 表示剩余的数个数

    for i in range(target+1):
        for j in range(n+1):
            print "%4d" % dp[i][j],
        print "\n"
    
    return dp[target][n]    

if __name__ == "__main__":
    num = [3, 24, 4, 12, 5, 2]
    target = 9
    if hasSubSetSumRecursion(num, len(num), target):
        print "Recursion Function: Found a sub set in num!"
    else:
        print "Recursion Function: No sub set in num!"

    if hasSubSetSumDP(num, len(num), target):
        print "DP Function: Found a sub set in num!"
    else:
        print "DP Function: No sub set in num!"
