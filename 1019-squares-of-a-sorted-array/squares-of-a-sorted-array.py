class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # l=[]
        # for i in range(len(nums)):
        #     l.append(nums[i]*nums[i])
        # return sorted(l)  
        pos_list=[]
        neg_list=[]
        i=0
        j=0
        result=[]
        for k in range(len(nums)): # segregation
            if nums[k]<0:
                neg_list.append(nums[k]*nums[k])
            else:
                pos_list.append(nums[k]*nums[k])
        neg_list= neg_list[::-1]   
        while i<len(neg_list) and j<len(pos_list):
            if pos_list[j]>neg_list[i]:
                result.append(neg_list[i])
                i+=1
            else:
                result.append(pos_list[j])
                j+=1
        while i<len(neg_list):
            result.append(neg_list[i])
            i+=1
        while j<len(pos_list):
            result.append(pos_list[j])
            j+=1
        return result