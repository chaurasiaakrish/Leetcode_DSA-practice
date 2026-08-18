class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod=nums[0]
        max_prod=nums[0]
        min_prod=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            prod=nums[i]                
            max_prod=max_prod*nums[i]   
            min_prod=min_prod*nums[i]   
            maxx=max(prod,max(max_prod,min_prod))
            minn=min(prod,min(max_prod,min_prod))
            max_prod=maxx
            min_prod=minn
            res=max(res,max(maxx,minn))
        return res  