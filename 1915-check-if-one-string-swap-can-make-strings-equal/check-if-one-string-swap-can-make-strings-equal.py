class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count=0
        if len(s1)==len(s2):
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    count+=1
                else:
                    i+=1
            if count>2:
                return False
            else:
                freq1={}
                freq2={}
                for i in s1:
                    freq1[i]=freq1.get(i,0)+1
                for j in s2:
                    freq2[j]=freq2.get(j,0)+1
                if freq1==freq2:
                    return True
                else:
                    return False    
        else:
            return False    