class TrieNode: # extra class used to make trie nodes
    def __init__(self):
        self.children = {} # dict / hashmap used to locate child trie nodes of curr trie node
        self.is_end = False # bool used to determine if curr char trie node represents last char in a word or not 

# time : O(n) where n is the length of the passed in word 
# space : O(t+n) where t is the total num of trie nodes created + n which is th recursion call stk which goes until i == len(word) == n 
class WordDictionary:

    def __init__(self):
        self.root = TrieNode() # make root trie node 

    def addWord(self, word: str) -> None:
        curr = self.root # get curr root trie node

        for char in word: # for each char in passed in word 
            if char not in curr.children: # if not a child node in curr trie node
                curr.children[char] = TrieNode() # make it one by creating the trie node
            
            curr = curr.children[char] # and updating the curr trie to continue and add the rest of the chars below 
        curr.is_end = True # last trie node we create for curr word becomes the last char that makes up the word so mark the bool for that node to be True

    def search(self, word: str) -> bool:
        
        curr = self.root # ref root trie node 

        def dfs(i, curr): # define DFS to traverse the trie 
            if i == len(word) and curr.is_end: # if we evaluated the entire word that we are searching for and the ending node is actually the end of the word
                return True # then we know word was actually added - return true 
            if i == len(word) and curr.is_end == False: # otherwise the word we are looking for is only a prefix to a longer word 
                return False # return false in that case 


            curr_word = word[i] # otherwise we didn't finish processing each char in passed in word to look for 
            
            if curr_word == ".": # so if char is "."
                for child in curr.children: # then it can be any char after curr char so run DFS on each possbile character "." can represent 
                    if dfs(i+1, curr.children[child]): # if any path can returns true, then we can find the word from that path, so return True
                        return True
            
            if curr_word not in curr.children: # otherwise its just a regular char so if curr char node's children doesn't contain the next char we are looking for, then its impossbile to make that word 
                return False
            
            res = dfs(i+1, curr.children[curr_word]) # otherwise it's possbile so run DFS to see if we can make the rest (char i+1 to end)
            return res  # return the res of that 
        return dfs(0, curr) # start the DFS on first char on passed in word to look for and trie node of root.
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)