class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        summ = 0
        length = 0
        res = float("inf")
        for j in range(len(nums)):
            summ=summ+nums[j]
            while(summ>=target):
                length=j-i+1
                res=min(res,length)
                summ=summ-nums[i]
                i+=1
        if res==float("inf"):
            return 0
        else:
            return res     
