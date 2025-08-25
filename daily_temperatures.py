class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0 for i in range(n)] # initialize answers array 
        stack = [] # initialize stack for tracking an array of size 2 - day number and how hot it was that say 
        for i,temp in enumerate(temperatures): # for each temp and day of that temp
            # if we have a stack of temps already and curr temp is > than most recent tmp that has not seen a bigger temp yet
            while stack and temp > stack[-1][1]: 
                index, tmp = stack.pop() # remove that recent day and temp from stack since we finally seen one
                num_days = i - index # calculate how long it's been
                answers[index] = num_days # save how long it's been in its correct answers array slot
            # otherwise stack is empty or the curr tmp isn't actually hotter than most recent temp - just add onto stack
            stack.append([i,temp]) 
        return answers # return populated answers array at end