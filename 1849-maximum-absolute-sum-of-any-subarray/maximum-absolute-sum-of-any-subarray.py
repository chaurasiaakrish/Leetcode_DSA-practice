class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]

        max_sum = nums[0]
        min_sum = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            curr_min = min(nums[i], curr_min + nums[i])

            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)

        return max(max_sum, abs(min_sum))