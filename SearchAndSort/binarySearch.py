#! /usr/bin/python
# -*- conding: UTF-8 -*-

def binarySearchRec(arr, l, r, x):

    if l <= r:
        mid = l + (r-l) / 2
        
        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return binarySearchRec(arr, l, mid-1, x)
       
        else:
            return binarySearchRec(arr, mid+1, r, x)
    
    return -1


def binarySearch(arr, l, r, x):
    
    while l <= r:
        mid = l + (r-l) / 2
        
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            r = mid - 1

        else: 
            l = mid + 1

    return -1


if __name__ == "__main__":

    arr = [2, 3, 4, 10, 40]
    x = 10

    result1 = binarySearchRec(arr, 0, len(arr)-1, x)
    result2 = binarySearch(arr, 0, len(arr)-1, x)

    if result1 != -1:
        print "Rec function: Element is present at index %d" % result1
    else:
        print "Rec function: Element not found!"


    if result1 != -1:
        print "Iterate function: Element is present at index %d" % result1
    else:
        print "Iterate function: Element not found!"

