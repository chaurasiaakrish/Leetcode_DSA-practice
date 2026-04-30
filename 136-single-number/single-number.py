class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=0
        count=0
        for i in range(len(nums)):
            n=nums[i]^n 
        return n      