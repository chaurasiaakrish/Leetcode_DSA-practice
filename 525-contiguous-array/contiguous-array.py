class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        summ = 0
        maxi = 0

        # prefix_sum -> first index
        first = {0: -1}

        for i in range(len(nums)):

            if nums[i] == 0:
                summ -= 1
            else:
                summ += 1

            if summ in first:
                length = i - first[summ]
                maxi = max(maxi, length)
            else:
                first[summ] = i

        return maxi


