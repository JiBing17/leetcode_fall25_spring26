class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # populate mapping with regex to words that match that expression as values
        # BFS with word, get every possible regex pattern, see if any words OTHER words match, if so add those words to q as well
        # for each level in BFS, add 1 to the transformation sequence

        if endWord not in wordList: # not possbile, return 0
            return 0

        # populate adjlist where key = word with 1 spot that can be ANYTHING and value is array of words that differ by only that 1 spot 
        wordList.append(beginWord) 
        mapping = {}
        for word in wordList: # for each word
            for j in range(len(word)): # for each char in curr word
                pattern = word[:j] + "*" + word[j+1:] # make all possbile regex pattern for curr word
                if pattern not in mapping: # populate
                    mapping[pattern] = []
                mapping[pattern].append(word)

        num_of_transformations = 1 # init num of words
        q = deque() # deque for BFS 
        q.append(beginWord) # add start word to queue
        visited = set() # visited set to prevent evaluating same word

        while q: # while q is not empty ... 
            q_size = len(q) # process elements in curr layer 
            for i in range(q_size):
                curr_word = q.popleft() # get word
                if curr_word == endWord: # we transformed it to end, return count 
                    return num_of_transformations
                for j in range(len(curr_word)): # otherwise ... 
                    pattern = curr_word[:j] + "*" + curr_word[j+1:] # find ALL patterns
                    related = mapping[pattern] # find other words that differ by 1 letter

                    for word in related:
                        if word not in visited: # if we haven't processed it yet
                            q.append(word) # we can choose to transform curr word to this word (can choose multiple paths for that layer , don't care what word just if we can or NOT)
                            visited.add(word) # prevent revaluation of same word
            num_of_transformations += 1 # add to num of words we need to reach end
        return 0 # case where end word is in list but we can NEVER reach there with just transforming 1 letter at a time

            
