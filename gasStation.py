# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:28:35 2015

There are N gas stations along a circular route, where the amount of gas at 
station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
from station i to its next station (i+1). You begin the journey with an empty 
tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit 
once, otherwise return -1.

Note:
The solution is guaranteed to be unique.

Tags Greedy

idea:

如果sum(gas) < sum(cost)则无解, 否则必定有解。
remain是油箱里剩下的油，如果加上gas[i]也到不了下一站，那么继续将下一站设置为起点。
很巧妙。






@author: Neo
"""

class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        startIndex = 0
        remain = 0
        
        for i in xrange(n):
            if gas[i] + remain < cost[i]:
                startIndex = i + 1
                remain = 0
            else:
                remain += gas[i] - cost[i]
        
        return startIndex
        
        
        