class TrieNode: # define class to make trie node object
    def __init__(self):
        self.children = {} # store the diff char nodes it can have for its child nodes
        self.is_end_char = False # determine if this char node is end of a word

# time: O(n) for each operaiton where n is the passed in str length
# space: O(t) where t is total num of trie nodes created (space for making trie data structure)
class Trie:

    def __init__(self):
        self.root = TrieNode() # init a root trie node to use a ref when traversing in other functions

    def insert(self, word: str) -> None:

        curr = self.root # find ref to root node in trie

        for char in word: # each char in passed in word
            if char not in curr.children: # if not a child node of curr node
                curr.children[char] = TrieNode() # make it a child of curr trie node by creating a new one with that char and adding it to curr's child nodes
            curr = curr.children[char] # move to that child char node
        
        curr.is_end_char = True # set the last trie node created as True for it's bool property to indicate its the last char node that makes up a word
        

    def search(self, word: str) -> bool:
        curr = self.root # find ref to root

        for char in word: # for each char in passed in word
            if char not in curr.children: # if we can't find word in path, then its invalid word to search and find in trie
                return False
            curr = curr.children[char] # otherwise we keep traversing the trie
        return curr.is_end_char # only return True if the last char node we are on is the end of a word (search needs to be complete)

    def startsWith(self, prefix: str) -> bool: # similar to search but not strict with ending
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True # always return True if we can make up that word even if there is more ahead (looking for just the prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)