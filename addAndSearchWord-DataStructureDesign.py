# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 10:32:10 2015

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string 
containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

click to show hint.

Tags: Backtracking Data Structure Trie
Similar Problems (M) Implement Trie (Prefix Tree)

idea:
字典树（Trie），通配符.可以用枚举实现。


@author: Neo
"""

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
            if letter not in node.childs:
                node.childs[letter] = TrieNode()
            node = node.childs[letter]
        node.isWord = True
        

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.find(word,self.root)
    
    def find(self,word,node):
        if word == "":
            return node.isWord
            
        if word[0] == ".":
            for nd in node.childs.keys():
                if self.find(word[1:],node.childs[nd]):
                    return True
        else:
            child = node.childs.get(word[0])
            if child:
                return self.find(word[1:],child)
        return False

class TrieNode:
    def __init__(self):
        self.childs = dict()
        self.isWord = False


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
wordDictionary.addWord("a")
print wordDictionary.search("a")