class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      i=0
      freq={}
      res=0
      for j in range(len(s)):
        freq[s[j]]=freq.get(s[j],0)+1
        if (len(freq)!=(j-i+1)):
            freq[s[i]]-=1
            if freq[s[i]]==0:
                del freq[s[i]]
            i+=1
        else:
            length=j-i+1
            res=max(length,res) 
      return res      