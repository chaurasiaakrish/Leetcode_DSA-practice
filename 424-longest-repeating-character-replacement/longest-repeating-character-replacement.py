class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        freq = {}
        maxi = 0
        res = 1
        diff = 0
        for j in range(i, len(s)):
            freq[s[j]] = freq.get(s[j], 0) + 1
            maxi = max(freq.values())
            diff = (j - i + 1) - maxi
            if diff <= k:
                res = max((j - i + 1), res)
            else:
                freq[s[i]]-=1
                if freq[s[i]]==0:
                    del freq[s[i]]
                i+=1
        return res                
