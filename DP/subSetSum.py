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
    

if __name__ == "__main__":
    num = [3, 24, 4, 12, 5, 2]
    target = 9
    if hasSubSetSumRecursion(num, len(num), target):
        print "Found a sub set in num!"
    else:
        print "No sub set in num!"
