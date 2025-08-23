class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_map = {} # dict used for getting the count of each character in the s string
        # for each character in s, make a key (character value) and value (how many times we have seen that character already)
        for char in s: 
            if char not in s_map:
                s_map[char] = 0
            s_map[char] += 1

        t_map = {} # dict used for getting the count of each character in the t string
        # for each character in t, make a key (character value) and value (how many times we have seen that character already)
        for char in t:
            if char not in t_map:
                t_map[char] = 0
            t_map[char] += 1

        return s_map == t_map # return true of false if the counts of each letter is exactly the same