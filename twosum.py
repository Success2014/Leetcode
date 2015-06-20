__author__ = 'Neo'

'''
idea: use dictonray for fast search.
Use dictionary to record the index of the found item.
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

