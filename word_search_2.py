class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

# time: O(m*n*4*3^(t-1) + s) where t = max length of word length and s is time it takes to make trie ds
# space: (s) total num of trie nodes created     

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # make trie data struct based on words input arr given
        self.root = TrieNode() 
        n_rows = len(board)
        n_cols = len(board[0])

        for word in words:
            curr = self.root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                
                curr = curr.children[char]

            curr.is_end = True

        # dfs used to traverse all possible words that the curr path in 2d grid can make
        def dfs(i, j, visited, curr, path):

            if curr.is_end: # if path makes from start to now is a word
                self.res.add(path) # add to result array the path AND CONTINUE (possbile words still in this path where curr word is prefix to a bigger word)
            
            if i >= n_rows or i < 0 or j >= n_cols or j < 0 or (i,j) in visited: # abandon path if out of bounds in 2d grid or we are in cycle
                return
            
            if board[i][j] not in curr.children: # also abandon path if character we are on doesn't make up any words using the trie data strucuture (return from path) 
                return
            
            visited.add((i,j)) # otherwise there are word(s) that still can be made up with curr DFS path, so see if we can make up those words going in ALL possbile directions
            dfs(i+1, j, visited, curr.children[board[i][j]], path + board[i][j])
            dfs(i-1, j, visited, curr.children[board[i][j]], path + board[i][j])
            dfs(i, j+1, visited, curr.children[board[i][j]], path + board[i][j])
            dfs(i, j-1, visited, curr.children[board[i][j]], path + board[i][j])
            visited.remove((i,j)) # backtrack

        self.res = set() # prevent duplicate words since its possbile for words to appear on grid in diff places so two diff DFS can make same word 
        visited = set() # constant time to check if we revisited pos or not
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c, visited, self.root, "") # run DFS startign on each cell since word can be found starting from anywhere 
        return list(self.res) # return as arr at end
                   

        
            

                    
                


        # for each word
        # run DFS ttrying to find that word trying all possbile paths (n*m dfs calls)
        # if any return True, then we can add that word to res arr to return
        
        # brute force solution
        # time: O(k*m*n * 4^(L)) where k is total num of words given, m is num of rows, n is num of cols, and L is the avg length of a word we are looking for
        # space : O(T) whre T is max lengh of any word in words arr

        self.res = []
        visited = set()

        n_rows = len(board)
        n_cols = len(board[0])

        def dfs(i,j, k, n, visited):
            if k == n:
                return True
            
            if i >= n_rows or i < 0 or j < 0 or j >= n_cols or (i,j) in visited:
                return False
            
            if board[i][j] != word[k]:
                return False
        
            visited.add((i,j))

            down = dfs(i+1, j, k+1, n, visited)
            up = dfs(i-1, j, k+1, n, visited)
            right = dfs(i, j+1, k+1, n, visited)
            left = dfs(i, j-1, k+1, n, visited)

            visited.remove((i,j))

            return ( down or up or right or left)

        
        for word in words: # k 
            found = 0
            n = len(word)
            for i in range(n_rows): # m
                for j in range(n_cols): # n
                    if dfs(i,j, 0, n, visited):
                        self.res.append(word)
                        found = 1
                        break
                if found:
                    break           
        return self.res
