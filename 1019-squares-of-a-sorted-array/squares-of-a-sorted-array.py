class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        j=0
        pos=[]
        neg=[]
        l=[]
        for k in range(len(nums)):
            if nums[k]<0:
                neg.append(nums[k])
            else:
                pos.append(nums[k])

        if len(pos)==0:
            for m in range(len(neg)):
                neg[m]=neg[m]**2
            return neg[::-1]  

        elif len(neg)==0:
            for n in range(len(pos)):
                pos[n]=pos[n]**2
            return pos
            
        for a in range(len(neg)):
            neg[a]=neg[a]**2
        neg.reverse()
        for b in range(len(pos)):
            pos[b]=pos[b]**2    

        while(i<len(neg) and j<len(pos)):
            if neg[i]<pos[j] :
                l.append(neg[i])
                i+=1      
            else:
                l.append(pos[j])  
                j+=1
        while(i<len(neg)):
                l.append(neg[i])
                i += 1
        while(j < len(pos)):
                l.append(pos[j])
                j += 1    

        return l