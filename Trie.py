from collections import defaultdict
import os

class Trie:
    """
    Implement a trie with insert, search, and startsWith methods.
    """
#    TAG=[]
    def __init__(self):
        self.root = defaultdict()
        self.TAG = []
    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word, tag):
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        if current == None :
            current = {}
        current.setdefault(tag)
        self.TAG.append(tag)
       
    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        current = self.root
        for letter in word:
            if current ==None:
                return "-"
            if letter not in current:
                return "-"
            current = current[letter]
        if current ==None:
            return "-"
        for tag in self.TAG:
            if tag in current:
                #print "O"
                return tag
        return "-"
		
    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    
    def startsWith(self, prefix):
        #TAG = []
        #TAG.append("A")
        #TAG.append("B")
        #TAG.append("C")

        current = self.root
        ANS = []
        A = []

        for letter in prefix:
            if letter in current:
                if current[letter] == {}:
                    #print "*"
                    break
                current = current[letter]
            else:
                return []
        if current == None:
            return []
        for letter in current:
            if letter not in self.TAG :
                A = self.startsWith(prefix+letter)
            else:
                if prefix not in ANS:
                    ANS.append(prefix)
            for x in A:
                ANS.append(x)
            A = []
        return ANS

    def delet(self, word):
        current = self.root
        SUB = self.startsWith(word)
        tags = []
        for i in range(len(SUB)):
            tags.append(self.search(SUB[i]))
        c = 0
        
        if (len(SUB)==1):
            L = ""
            New = []
            
            for letter in word:
                c = c+1
                if letter in current:
                    L =letter
                    if(c==len(word)):
                        #print "miay ?"
                        #print "?",L
                        current[L] = None
                    else:
                        current = current[letter]
        else:
            for letter in word:
                c = c+1
                #print "letter",letter
                if letter in current:
                    #print "current",current[letter]
                    if(c==len(word)):
                        current[letter] = {}
                    else:
                        current = current[letter]
                        
            for i in range(len(SUB)):
                if(SUB[i]!=word):
                    #print "=",SUB[i]
                    self.insert(SUB[i],tags[i])

# Now test the class
