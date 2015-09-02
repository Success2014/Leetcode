# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 09:58:10 2015

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
            if letter not in node.childs:
                node.childs[letter] = TrieNode()
            node = node.childs[letter]
        node.isWord = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for letter in word:
            if letter not in node.childs:
                return False
            node = node.childs[letter]
        return node.isWord

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            if letter not in node.childs:
                return False
            node = node.childs[letter]
        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")