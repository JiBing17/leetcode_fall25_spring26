class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = [] # intialize stack

        for tok in tokens: # for each token in array 
            if tok == "+" or tok == "-" or tok == "*" or tok == "/": # if its an operation
                second_operand = int(stack.pop()) # get last val seen
                first_operand = int(stack.pop()) # get second last val seen
                res = 0 # result val used to store result after doing operation 
                if tok == "+": # plus case
                    res = first_operand + second_operand
                if tok == "-": # minus case
                    res = first_operand - second_operand
                if tok == "*": # multiply case
                    res = first_operand * second_operand
                if tok == "/": # int division case
                    res = first_operand / second_operand
                stack.append(res) # add result back to stack for most recent val
            else:
                stack.append(tok) # otherwise its not an operation, we can just add to stack as last val seen

        return int(stack[0]) # at the end, resulting val after all operations will be the only val in stack