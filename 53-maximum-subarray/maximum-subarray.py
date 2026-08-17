class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ=0
        max_sum=nums[0]
        i=0
        while i<len(nums):
            summ=summ+nums[i]
            max_sum=max(max_sum,summ)
            if summ>=0:  
                i+=1
            else:
                summ=0
                i+=1
        return max_sum            