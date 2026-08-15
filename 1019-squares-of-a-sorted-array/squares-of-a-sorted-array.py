class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # l=[]
        # for i in range(len(nums)): # O(n)
        #     l.append(nums[i]*nums[i])
        # return sorted(l)    # O(nlogn)

        res=[]
        pos_list=[]
        neg_list=[]
        i=0
        j=0
        for k in range(len(nums)):
            if nums[k]<0:
                neg_list.append(nums[k]*nums[k])
            else:
                pos_list.append(nums[k]*nums[k])
        neg_list=neg_list[::-1]          
        while(i<len(pos_list) and j<len(neg_list)):
            if pos_list[i]>neg_list[j]:
                res.append(neg_list[j])
                j+=1
            else:
                res.append(pos_list[i])
                i+=1         
        while(j<len(neg_list)):
            res.append(neg_list[j])
            j+=1
        while(i<len(pos_list)):
            res.append(pos_list[i]) 
            i+=1 
        return res