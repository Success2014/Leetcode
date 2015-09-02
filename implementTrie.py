# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:29:06 2015

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

Tags: Data Structure Trie
Similar Problems: (M) Add and Search Word - Data structure design


Trie使用孩子表示法存储，TrieNode为字典树的节点，包含属性childs和isWord。

其中childs为dict，存储当前节点的后代节点；isWord为布尔值，表示当前节点是否存储了一
个单词。

Tags: Data Structure Trie
Similar Problems (M) Add and Search Word - Data structure design


@author: Neo
"""

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.childs = dict()
        self.isWord = False
        

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for letter in word:
            node = node.childs.get(letter)
            if node is None:
                return False        
        return node.isWord

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            node = node.childs.get(letter)
            if node is None:
                return False
        return True
            
        

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
print trie.search("key")