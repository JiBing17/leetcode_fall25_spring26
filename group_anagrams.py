class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {} # dict used where keys are char to count mappings and values are the words that fit that mapping
        for string in strs: # iterate through each string in strs
            char_to_count = {} # create mapping for each string
            for char in string: # populate the mapping
                if char not in char_to_count:
                    char_to_count[char] = 0
                char_to_count[char] += 1

            # get array of tuples where each tuple contains the letter and count of that letter in each word
            key = tuple(sorted(char_to_count.items()))
            if key not in anagrams: # that key will then be used to populate the anagram dict
                anagrams[key] = []
            anagrams[key].append(string)
    
        answers = [] # array for returning the answers 
        for key in anagrams: # for each key (char to count mapping)
            values = anagrams[key] # array of words that fit in the current anagram categ
            answers.append(values) # add that resulting array to answers array and move onto next anagram category of words
        return answers # return the populated answers array at end 