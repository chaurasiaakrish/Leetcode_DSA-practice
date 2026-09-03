class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        result=[]
        result.append(intervals[0])
        for i in range(1,len(intervals)):
            end=result[-1][1]
            start=intervals[i][0]
            if end>=start:
                result[-1][1]=max(end,intervals[i][1])
            else:
                result.append(intervals[i])  
        return result          