class MinStack:

    def __init__(self):
        self.order_stack = [] # 1st stack to keep track of order of adding to stack in constant time
        self.min_stack = [] # 2nd stack to keep track of min value so far in constant time
        

    def push(self, val: int) -> None:
        self.order_stack.append(val) # add to order stack
        if self.min_stack: # if min stack exists, find minimum between val in min stack vs current val to add
            min_val = min(self.min_stack[-1], val) 
        else:
            min_val = val # otherwise min val is just val we are planning to add

        self.min_stack.append(min_val) # add to min_stack


    def pop(self) -> None:
        self.order_stack.pop() # remove top element of order stack to update top val
        self.min_stack.pop() # remove top element of min stack to update min val poptentially


    def top(self) -> int:
        return self.order_stack[-1] # return top most element in order stack in 

    def getMin(self) -> int:
        return self.min_stack[-1] # return top most element in min stack for min val seen so far 