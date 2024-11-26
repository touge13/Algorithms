class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key = lambda x: x[0])
        res = [intervals[0]]
        for current in intervals[1:]: 
            if current[0] <= res[-1][1]: 
                res[-1][1] = max(current[1], res[-1][1]) 
            else: 
                res.append(current)
        return res 
