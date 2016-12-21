#! /usr/bin/python
# -*- coding: UTF-8 -*-

def lis(numbers):
    n = len(numbers)
    dp = [1] * n
    maxLen = 1
    for i in range(1, n):
        for j in range(i):
            if numbers[i] > numbers[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    for i in range(n):
        if maxLen < dp[i]:
            maxLen = dp[i]
    return maxLen

if __name__ == "__main__":
    numbers = [10, 22, 9, 33, 21, 50, 41, 60]
    print "Length of LIS is ", lis(numbers)
