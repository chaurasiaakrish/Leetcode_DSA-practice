class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        count=0
        maxi=0
        while(i<len(nums)):
            if nums[i]==1 :
                count+=1
                i+=1
            else:
                maxi=max(maxi,count)  
                count=0
                i+=1
        return max(maxi,count)     