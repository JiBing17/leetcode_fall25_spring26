class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [] # initialize array to return at end 
        stack = [] # will contain variation of parentheses to add to res
        self.add(0,0, n, res, stack) # call recursive "add" function starting from 0 right and left brackets
        return res # return the populated res array after the recursive calls
        
    def add(self, l_bracket, r_bracket, n, res, stack): # recursive function to find and add all valid variations 

        # we have completed a variation of parentheses where left and right brackets are equal to input n 
        if l_bracket == r_bracket == n: 
            res.append("".join(stack)) # add this variation from stack onto res array
            return 

        if l_bracket < n: # add an opening parenthesis if we haven't reach n parentheses yet
            stack.append("(") # add opening to variation stack 
            # recursively call given the updated variation stack (choose to add left bracket in this case)
            self.add(l_bracket+1, r_bracket, n, res, stack) 
            stack.pop() # remove the resulting variation after the recursive calls so we can do another 

        if r_bracket <  l_bracket: # case to add closing bracket if only we have less close brackets compared to open ones
            stack.append(")") # add closing to variation stack 
            # recursively call given the updated variation stack (choose to add right bracket in this case)
            self.add(l_bracket, r_bracket + 1, n, res, stack) 
            stack.pop() # remove the resulting variation after the recursive calls so we can do another 