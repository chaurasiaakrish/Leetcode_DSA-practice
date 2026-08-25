class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        left=0
        right=0
        for i in range(len(nums)):
            right=total-left-nums[i]
            if left==right:
                return i
            else:
                left+=nums[i]
        return -1