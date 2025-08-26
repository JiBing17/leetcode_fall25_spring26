class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position) # num of cars
        stack = [] # stack used to indentify car fleets and most recent car fleet's mph to reach target

        # sort arrays based on position in descending order - we do this because when we make a car a car fleet, we need to make sure all cars ahead of it is already processed
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True) 
        
        for i in range(n): # for each car starting from one closest to target
            dis = target - cars[i][0] # find distance needed 
            num_hours = dis / cars[i][1] # find mph needed to reach that distance
            if stack and stack[-1] >= num_hours: # if there is a fleet in front of current car, see if we can catch up to become one fleet
                continue # case: we caught up and became a fleet with the slower moving car, no need to add another fleet 
            else:
                stack.append(num_hours) # case: we didn't catch up so we become a fleet which is is moving at num_hours var - this car behind it will determine if it will become a car fleet with this one given it's num_hours

        return len(stack) # return the number of car fleets at end 