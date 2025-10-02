class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        mapping = {i: [] for i in range(numCourses)} # map for course to prereqs  
        visited = set() # course path taken for curr call stack
        done = set() # courses that are already evaluated
        self.path = [] # path to return 

        for crs, prereq in prerequisites: # populate the mapping
            mapping[crs].append(prereq)
        
        def dfs(course): # helper dfs to add to path

            if course in visited: # cycle return False - not vaid path
                return False

            if mapping[course] == [] and course not in done: # base case no prereqs for course and haven't evaluated this course yet 
                done.add(course) # add course to indicate it's been evaluated
                self.path.append(course) # add to path on the way back 
                return True

            visited.add(course) # add curr course to visited 
            for prereq in mapping[course]: # for all prereqs of curr course
                if not dfs(prereq): # if any prereqs can't be finished
                    return False # return false

            visited.remove(course) # remove from visited for next dfs call
            mapping[course] = [] # can conclude this course can be finished with its prereqs so set prereqs to empty as if it didn't have any - helpful for next iteration
            if course not in done: # add course that had prereqs to path since valid 
                done.add(course) # mark it as evauated to prevent double check
                self.path.append(course) # add to path
            return True # return true for valid course to finish
        
        for i in range(numCourses): # try each course to with dfs
            if not dfs(i): # if any can't be finished return []
                return []

        return self.path # otherwise return path