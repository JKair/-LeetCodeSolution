Merge Intervals
================
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].


这道和`Insert Interval`的不一样在于，这次已经是插入好了，让我们来处理合并的事情。

我们可以先对整个vector进行排序，然后用一个新的容器装着结果，每次都和结果容器的最后一个比对区间，处理包含情况。


```
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    static bool comp(const Interval &a, const Interval &b) {
        return (a.start < b.start);
    }
    vector<Interval> merge(vector<Interval>& intervals) {
        vector<Interval> res;
        if (intervals.empty()) return res;
        sort(intervals.begin(), intervals.end(), comp);
        res.push_back(intervals[0]);
        for (int i = 1; i < intervals.size(); i++) {
            if (res.back().end >= intervals[i].start) {
                res.back().end = max(intervals[i].end, res.back().end);
            } else {
                res.push_back(intervals[i]);
            }
        }

        return res;
    }
};
```


相似题目[Insert Interval](./Insert Interval.md)
