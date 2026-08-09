class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0
        while fast< len(nums):
            slow=nums[slow]
            fast=nums[nums[fast]]
            if fast==slow:
                slow=0
                while slow!=fast:
                    slow=nums[slow]
                    fast=nums[fast]
                return slow    



        # freq={}
        # for n in nums:
        #     freq[n]=freq.get(n,0)+1
        # for value in freq:
        #     if freq[value]>1:
        #         return value
