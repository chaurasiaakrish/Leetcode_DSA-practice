class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        res = float("inf")
        summ = 0
        length = 0
        while high < len(nums):
            summ = summ + nums[high]
            while summ >= target:
                length = (high - low) + 1
                res = min(res, length)
                summ = summ - nums[low]
                low += 1
            high += 1
        if res == float("inf"):
            return 0
        else:
            return res