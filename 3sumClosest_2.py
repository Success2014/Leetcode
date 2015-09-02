# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 17:43:06 2015

@author: Neo
"""

mindf = 2147483648
        nums.sort()
        for i in xrange(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    s = nums[i] + nums[left] + nums[right]
                    df = abs(s - target)
                    if df == 0:
                        return target
                    if s < target:
                        if df < mindf:
                            mindf = df
                            flag = -1
                        left += 1
                    else:
                        right -= 1
                        if df < mindf:
                            mindf = df
                            flag = 1
                        
                
        
        return target + flag * mindf