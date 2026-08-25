class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        summ=0
        count=0
        freq={}
        freq[summ]=freq.get(summ,0)+1
        for i in range(len(nums)):
            summ=summ+nums[i]
            need=summ-k
            if need in freq:
                count+=freq[need]
                freq[summ]=freq.get(summ,0)+1
            else:
                freq[summ]=freq.get(summ,0)+1
        return count        
            
