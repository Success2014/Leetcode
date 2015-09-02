# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 10:22:04 2015

@author: Neo
"""

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = dict()
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
            child = node.children.get(letter,None)
            if child is None:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for letter in word:
            child = node.children.get(letter, None)
            if child is None:
                return False
            node = child
        return node.isWord
        
        
        

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            child = node.children.get(letter, None)
            if child is None:
                return False
            node = child
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")