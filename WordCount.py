#!/usr/bin/python
# -*- encoding: utf-8 -*-

import re

def wordCount(filename):
    wordsDict = {}
    words = []
    
    with open(filename, 'r') as f:
        for line in f:
            re.sub(r'[\W]', '', line)
            words.extend(line.strip().split(' '))
    for word in words:
        if word not in wordsDict:
            wordsDict[word] = 1
        else:
            wordsDict[word] += 1
    return wordsDict

if __name__ == '__main__':
    filename = "test.txt"
    wordsDict = wordCount(filename)
    print 'In file', filename
    print 'Frequency of each word:'
    for key, value in wordsDict.items():
        print '%s : %d' % (key, value)


