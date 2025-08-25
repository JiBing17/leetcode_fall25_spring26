class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        mapping = {} # initalize dict to mapp closing bracket's to their respective opening brackets
        mapping["}"] = "{"
        mapping["]"] = "["
        mapping[")"] = "("
        stack = [] # initialize empty stack to find most recent opening bracket type 

        for char in s: # go through each char in s
            if char == "{" or char == "[" or char == "(": # add any opening bracket to stack
                stack.append(char) 
            else: # case if it's a closing bracket 
                mapped_match = mapping[char] # find the closing bracket's opening counter part through dict
                if len(stack) == 0: # case if there is no opening bracket in the stack to begin with to match it, return false
                    return False
                recent = stack.pop() # get the most recent opening bracket
                if recent != mapped_match: # see it matches, if not also return false
                    return False

        return len(stack) == 0 # return true if no more opening brackets left to close at end