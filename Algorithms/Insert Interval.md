Insert Interval
==============

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

这道题给我们一个区间，然后让我们合并进原本的区间数组，要做的就是，如果有重叠的要合并。


这道题的难点在于处理重叠区域的问题。

1. 遍历区间
1. 如果发现区间重叠了，分为四种情况，新区间包含数组区间的左边或者右边或者全包含或者被包含。
1. 新区间被全包含，intervals不变直接返回。
1. 新区间全包含intervals里的某个区间，或者某几个区间，那么新区间的start和end是不变的，要跳过当前循环的旧区间不理，直到找到重点。
1. 新区间的左边被包含进去或者右边被包含进去，这两种情况是相同的，我们只要将新区间的左右两端给扩大到包含这两个区间就可以了

C++:
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
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
        int i = 0;
        vector<Interval> res;
        for (; i < intervals.size(); i++) {
              if (newInterval.start <= intervals[i].end) {
                  if (newInterval.end < intervals[i].start) {
                      break;
                  }
                  newInterval.start = min(newInterval.start, intervals[i].start);
                  newInterval.end = max(newInterval.end, intervals[i].end);
              } else {
                  res.push_back(intervals[i]);
              }
        }
        res.push_back(newInterval);
        for (; i < intervals.size(); i++) {
            res.push_back(intervals[i]);
        }

        return res;
    }
};
```

python:

```
class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        start = newInterval.start
        end = newInterval.end
        result = []
        i = 0
        while i < len(intervals):
            if start <= intervals[i].end:
                if end < intervals[i].start:
                    break
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
            else:
                result.append(intervals[i])
            i += 1
        result.append(Interval(start, end))
        result += intervals[i:]
        return result
```
