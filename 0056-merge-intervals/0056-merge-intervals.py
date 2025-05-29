class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mergedIntervals = []
        intervals.sort(key= lambda interval: interval[0])
    
        for interval in intervals:
            if not mergedIntervals or mergedIntervals[-1][1] < interval[0]:
                mergedIntervals.append(interval)
            else:
                mergedIntervals[-1][1] = max(mergedIntervals[-1][1], interval[1]) 
            
        # TODO: Write your code here
        return mergedIntervals
