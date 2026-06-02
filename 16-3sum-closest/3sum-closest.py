class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        mini=float("-inf")
        maxi=float("inf")
        diff=0
        summ=0
        total=0
        nums.sort()
        i=0
        j=i+1 
        k=len(nums)-1
        while(i<len(nums)-2):
            while(j<k):
                total=nums[i]+nums[k]+nums[j]
                if total==target:
                    return total
                elif total<target:
                    diff=total-target
                    if max(mini,diff)==diff:
                        mini=diff
                        j+=1
                    else:
                        j+=1    
                elif total>target:
                    diff=total-target
                    if min(maxi,diff)==diff:
                        maxi=diff
                        k-=1
                    else:
                        k-=1                
            i+=1
            j=i+1        
            k=len(nums)-1
        if min(maxi,abs(mini))==maxi:
            return maxi+target
        else:
            return target+mini        