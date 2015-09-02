# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 10:56:56 2015

@author: Neo
"""

class TrieNode():
    def __init__(self):
        self.children = dict()
        self.isWord = False
        
        
class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.root = TrieNode()
        

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isWord = True
        

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        node = self.root
        return self.find(word,node)
    
    def find(self, word, node):
        if word == "":
            return node.isWord
        if word[0] == ".":
            for letter,nd in node.children.items():
                if self.find(word[1:],nd):
                    return True
            
        else:
            child = node.children.get(word[0])
            if child:
                return self.find(word[1:], child)
        return False
        
        

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("a")
print wordDictionary.search("a")