__author__ = 'Neo'

'''
Given an array of integers, find two numbers such that they add up to a 
specific target number.

The function twoSum should return indices of the two numbers such that 
they add up to the target, where index1 must be less than index2. 
Please note that your returned answers (both index1 and index2) are not 
zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

Tags Array Hash Table
Similar Problems (M) 3Sum (M) 4Sum (M) Two Sum II - Input array is sorted 
(E) Two Sum III - Data structure design



idea: use dictonray for fast search.
Use dictionary to record the index of the found item.

如果分两步走，第一步先把所有的num作为key放到dictionary里面的话，要注意解决
key冲突的问题。比如[0,4,1,0]找0.有两个0，怎么存他们的地址。




'''

def twosum(num, target):
    if num == []:
        raise ValueError
    else:
        whole_list = {}
        for index_i in range(len(num)):
            if whole_list.get(target - num[index_i], None) == None:
                whole_list[num[index_i]] = index_i
            else:
                return (whole_list[target - num[index_i]] + 1, index_i + 1)


num = [0,4,3,0]
target = 0

x,y = twosum(num, target)
print x,y

