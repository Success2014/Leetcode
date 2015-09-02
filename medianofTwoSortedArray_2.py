# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 22:31:37 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        if (n1+n2)%2:
            return self.getK(nums1,nums2,(n1+n2+1)/2)
        else:
            return (self.getK(nums1,nums2,(n1+n2)/2) + self.getK(nums1,nums2,(n1+n2)/2+1))*0.5
        
    def getK(self,nums1,nums2,k):
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.getK(nums2,nums1,k)
        if n1 == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0],nums2[0])
            
        pa = min(k/2, n1)
        pb = k - pa
        
        if nums1[pa-1] < nums2[pb-1]:
            return self.getK(nums1[pa:],nums2,k-pa)
        else:
            return self.getK(nums1,nums2[pb:],k-pb)
            
        

sol = Solution()        
nums1 = [1,3,5,7]
nums2 = [2,4,6,8,10]
print sol.findMedianSortedArrays(nums1,nums2)
        
        
        