class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        #initialise the root Node
        self.root = Node()

    def insert(self, word: str) -> None:
        #for each letter in the word, check if it's already in the Trie, if not add it.
        node = self.root
        word = word.lower()
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node()   
            node = node.children[letter]

        #turn the endOfWord flag to true at the last
        node.endOfWord = True

    def search(self, word: str) -> bool:
        #if all the letter is in the trie and there's end flag is true then return true
        node = self.root
        word = word.lower()

        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]

        if node.endOfWord:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        #if all the letter is in the trie. no need to check for end flag. could use this in the search method for cleaner code?
        node = self.root
        prefix = prefix.lower()

        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]

        return True