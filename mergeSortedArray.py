# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 15:20:37 2015

Given two sorted integer arrays nums1 and nums2, merge nums2 into 
nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

Tags Array Two Pointers
Similar Problems (E) Merge Two Sorted Lists


合并A、B两个有序数组到A中。
从前向后放不行，那就从后向前放吧
Merge from the back to make use of the space.
Put the bigger value at the end.
Don't forget to merge the remaining elements.



@author: Neo
"""

def merge(A, m, B, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[k] = A[i]            
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1
    while j >= 0:
        A[k] = B[j]
        k -= 1
        j -= 1
    
    

