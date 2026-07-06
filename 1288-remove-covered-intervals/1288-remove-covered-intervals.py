class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key =lambda x:(x[0], -x[1]))
        a =0
        b =0
        for start ,end in intervals:
            if end>b:
                a+=1
                b= end
        return a


        