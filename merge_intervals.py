class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a: a[0]) # O(nlogn) sort
        i = 0
        j = len(intervals) - 1
        while i < j:
            if intervals[i][1] >= intervals[i+1][0]:
                if intervals[i][1] <= intervals[i+1][1]:
                    intervals[i][1] = intervals[i+1][1]
                intervals.pop(i+1)
                j -= 1
                i -= 1
            i += 1
        return intervals