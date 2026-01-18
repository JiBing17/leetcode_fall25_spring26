class Solution:
    def hammingWeight(self, n: int) -> int:

        # time: O(1)
        # space: O(1)

        counter = 0 # count the total num of set bits
        while n:
            counter += n % 2 # find if the first bit is a 1 or not and add that to counter if it is 
            n = n // 2 # change n by dividing by 2 so we can eval next bit to the right of curr one we just evaluated
        return counter # return that counter at end after "finishing all the bits"