class Solution:
    def checkValidString(self, s: str) -> bool:
        # greedy approach: keep track of min and max num of "(" we can have which can be diff due to "*".
        # if we ever have "(" < 0 then we can greedily say for all "*" that becomes ")", make it be empty instead since we don't ever want to go down that path
        # at end if min or max possbile "(" ever becomes 0, then we have a way of making strign s valid
        # if at any point the max num of "(" < 0, then there is NO way of making the string s valid since we will have more ")" than "(" at the moment even with "*" being "(" so return false if that ever happens

        # time: O(n)
        # space : O(1)

        min_left = 0 # min num of "(" we can have ( case where * becomes ")" )
        max_left = 0 # max num of "(" we can have ( case where * becomes "(" )
    
        for char in s:
            if char == "(": # update num of left parenthesis if we encounter a "("
                min_left += 1
                max_left += 1
            if char == ")": # update num of left parenthesis if we encounter a ")" 
                min_left -= 1
                max_left -= 1

            if char == "*": # update max AND min num of left parenthesis if we encounter "*"
                min_left -= 1
                max_left += 1

            if max_left < 0: # at any point if count of left parenthesis even with * being "(" ever becomes < 0, then there is TOO much right parenethesis, making curr string s invalid
                return False
            if min_left < 0: # at any point if min possbile parenthesis (when * is ")" ) becomes < 0, then we say every "*" is empty instead (reset) 
                min_left = 0

        if min_left == 0 or max_left == 0: # return True if any of these two paths have same amount of left and right parenthesis 
            return True
        return False # otherwise it's not possbile for this string to become valid due to uneven num of "(" and ")"

        
        # brute force solution : use stk to evaluate the str and try every possbile path when we encounter a *
        # "(" we add to stk
        # ")" we pop from stk
        # "*" run dfs with it being "(" and "*" and ")"
        # if any returns True, then it is possbile for string s to be valid 

        # time : O(3^n)
        # space : O(n)
        n = len(s)

        def dfs(i, stk):
            if i == n and len(stk) == 0:
                return True
            if i == n and len(stk) > 0:
                return False
            
            curr = s[i] 

            if curr == "(":
                stk.append("(")
                res = dfs(i+1, stk)
                stk.pop()                  # BACKTRACK
                return res

            elif curr == ")":
                if not stk:
                    return False
                stk.pop()
                res = dfs(i+1, stk)
                stk.append("(")            # BACKTRACK
                return res
                
            else:  # '*'
                # treat as '('
                stk.append("(")
                if dfs(i+1, stk):
                    stk.pop()
                    return True
                stk.pop()

                # treat as empty
                if dfs(i+1, stk):
                    return True

                # treat as ')'
                if stk:
                    stk.pop()
                    if dfs(i+1, stk):
                        stk.append("(")
                        return True
                    stk.append("(")

        return dfs(0, [])

                