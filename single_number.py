class Solution:
    def singleNumber(self, nums: List[int]) -> int:

            # time : O(n)
            # space : O(1)
            
            res = 0  # Initialize result to 0 since XOR with 0 returns the number itself

            for num in nums: # Iterate through each number in the list
                res = res ^ num # XOR current result with num; duplicate numbers cancel out

            return res # return the only num that's not a dup        