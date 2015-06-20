# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 14:48:41 2015

解题思路：
题目的要求是输出Unix下的最简路径，Unix文件的根目录为"/"，"."表示当前目录，".."表示上级目录。
例如：
输入1：
/../a/b/c/./.. 
输出1：
/a/b
模拟整个过程：
1. "/" 根目录
2. ".." 跳转上级目录，上级目录为空，所以依旧处于 "/"
3. "a" 进入子目录a，目前处于 "/a"
4. "b" 进入子目录b，目前处于 "/a/b"
5. "c" 进入子目录c，目前处于 "/a/b/c"
6. "." 当前目录，不操作，仍处于 "/a/b/c"
7. ".." 返回上级目录，最终为 "/a/b"

使用一个栈来解决问题。遇到'..'弹栈，遇到'.'不操作，其他情况下压栈。


Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, 
such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".


@author: Neo
"""


def simplifyPath(path):
    ps = path.split('/')[1:]
    result = []
    for letter in ps:
        if letter == "..":
            if result:
                result.pop()
        elif letter == "" or letter ==".":
            pass
        else:
            result.append(letter)
    return '/' + '/'.join(result)
    
        
path = "/a/./b/../../c/"
path1 = "/../a/b/c/./.."
path2 = "/../"
path3 = "/home//foo/"
print simplifyPath(path3)



















