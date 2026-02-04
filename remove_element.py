class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # have a index to indicate next pos to overwrite to
        # index will increment if nums are NOT val
        # if it is val, then it wont advance so the next num that ISNT val will overwrite that index there
        # return the num of nums seen that isn't val

        # time : O(n)
        # space : O(1)
        n = len(nums)

        k = 0

        for i in range(n):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k
    
