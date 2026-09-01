class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq={0:1}
        count=0
        summ=0
        for i in range(len(nums)):
            summ=summ+nums[i]
            rem=summ%k
            if rem in freq:
                count+=freq[rem]
            freq[rem]=freq.get(rem,0)+1
        return count
