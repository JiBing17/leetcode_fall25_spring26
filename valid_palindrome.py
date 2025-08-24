class Solution:

    # helper function used to filter out text to just include lowercase letters and numbers
    def filter_text(self, s: str) -> str:
        new_string = "" # new text to return 
        for char in s: # for each character in string 
            if char.isdigit(): # if its a number
                new_string += char # add to new string
            elif char.isalpha(): # if its a letter
                new_string += char.lower() # add lowercase version of it to string 
        return new_string # return the new string

    def isPalindrome(self, s: str) -> bool:
        filtered_word = self.filter_text(s) # filter out the given s string
        l,r = 0, len(filtered_word)-1 # intialize 2 pointers, one at start of new string and one at end
        while l < r: # keep going until right passes left pointer
            if filtered_word[l] != filtered_word[r]: # if the two characters within the two pointers are diff, return false
                return False
            l += 1 # advance left pointer to the right
            r -= 1 # advance right pointer to the left 
        return True # end of check, actually a valid palindrome 