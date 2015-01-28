#我的第一种解法，严重超时
class Solution:
    def insert(self, intervals, newInterval):
        result = []
        for x in intervals:
        	if not (x.start > newInterval.end or x.end > newInterval.start):
        		newInterval.start = min(newInterval.start,x.start)
        		newInterval.end = max(newInterval.end,x.end)
        	else:
        		result.append(x)
        result.append(newInterval)
        return result
#我的第二种解法，想办法去除了所有不需要遍历的情况
class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        result = []
        start = newInterval.start
        end = newInterval.end
        x = 0
        while x<len(intervals):
            if start <= intervals[x].end:
                if intervals[x].start > end:
                    break
                start = min(start,intervals[x].start)
                end = max(end,intervals[x].end)
            else:
                result.append(intervals[x])
            x = x + 1
        result.append(Interval(start, end))
        result += intervals[x:]
        return result