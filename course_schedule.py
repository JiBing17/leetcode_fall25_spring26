class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()

        mapping = {i: [] for i in range(numCourses)} # define prereqs for each course i

        for crs, pre in prerequisites: # populate hash map wiht the prereqs for each course 
            mapping[crs].append(pre)
        
        def dfs(course): # helper to traverse through each course
            # there is a loop, can't finish all courses - return False 
            # (courses depend on each other)
            if course in visited: 
                return False
            # finished current course path - can finish return true
            if mapping[course] == []:
                return True 
            
            visited.add(course) # add course to visited path of courses

            for prereqs in mapping[course]: # for each of the prereqs of curr course
                if not dfs(prereqs): # see if we can finish those courses
                    return False # if not return false

            visited.remove(course) # remove curr course from path generated for next loop
            mapping[course] = [] # remove prereqs for curr course since we know we can finish
            return True # return true for that path

        for prereq in prerequisites: # for each of the courses that depend on others
            if not dfs(prereq[0]): # run dfs on those to see if we can finish them all
                return False # if not, return false
        return True # otherwise we can complete all the courses - return true at end