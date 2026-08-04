class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        freq = {}
        maxi = 0
        res = 0
        diff = 0
        for j in range(i, len(nums)):
            freq[nums[j]] = freq.get(nums[j], 0) + 1
            zeroes = freq.get(0,0)
            if zeroes <= k:
                res = max((j - i + 1), res)
            else:
                freq[nums[i]]-=1
                if freq[nums[i]]==0:
                    del freq[nums[i]]
                i+=1
        return res                
