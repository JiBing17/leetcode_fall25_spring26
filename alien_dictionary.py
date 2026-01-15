class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {c : set() for word in words for c in word} # adj_list to represent directed graph of which letters come before others
        n = len(words) # size of words in input
        for i in range(n-1): # go through input 
            w1 = words[i] # curr word
            w2 = words[i+1] # next word 

            min_l = min(len(w1), len(w2)) # find min length of two

            if len(w1) > len(w2) and w1[:min_l] == w2[:min_l]: # if curr_word is bigger AND second word is prefix of first
                return "" # then its invalid since smaller word in this case should be first
            
            for j in range(min_l): # otherwise look char by char of the 2
                if w1[j] != w2[j]: # when first letter differs
                    adj_list[w1[j]].add(w2[j]) # add to adj_list
                    break # eval second word as curr and the word after it 
        
        res = [] # res arr used to make str at end
        visited = {} # visited set to indicate if curr char is in current DFS path or not to let us know if path is valid to add to res

        def dfs(c):
            if c in visited: # if we have seen curr char
                return visited[c] # see if in curr path  
            visited[c] = True  # otherwise mark it as curr path 
             for neigh in adj_list[c]: # try continuing making valid ordering with ALL other chars that can come after curr
                if dfs(neigh): # if one of the orderings come to a loop (path is a cycle)
                    return True # then just return True (ordering doesn't make sense)
            visited[c] = False # otherwise we can make the ordering happen when adding curr char here, so set visited for curr char to be false
            res.append(c) # add to res arr the curr char


        for c in adj_list: # try to make valid ordering starting from every letter that has other letters that go after it  
            if dfs(c): # if any return's cycle in ordering, then return "" for impossbile case
                 return ""
        res.reverse() # otherwise, reverse res arr and return str since its post order DFS 
        return "".join(res)

            