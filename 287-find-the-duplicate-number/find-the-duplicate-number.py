class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        for value in freq:
            if freq[value]>1:
                return value
