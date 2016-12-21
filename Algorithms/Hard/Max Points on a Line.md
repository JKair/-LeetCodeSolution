Max Points on a Line
=========
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

这道题给我们一个数组的点，然后让我们算，在同一条线上的点最多是多少个。

解法：

1. 两点可以确定一条直线，根据公式`y = kx + b`。我们计算两个点，只要斜率是一样的，那么就说明这两线在同一直线上。
1. 然后，我们要处理两种特殊情况。
1. 一种是没有斜率的，也就是两个点的`x`是一样，就是说垂直于y轴的，这种情况，我们用一个特殊的数字将它们归类
1. 另外一种是相同的点的，遇到这种情况，我们需要一个参数去记录相同点有多少个。最后，我们需要将基于每个点的数字给计算出来最大的数字是多少。

```
/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
class Solution {
public:
    int maxPoints(vector<Point>& points) {
        map<float, int> flag;
        int res = 0;

        for (int i = 0; i < points.size(); i++) {
            flag.clear();
            flag[INT_MIN] = 0;
            int samePoint = 1;

            for (int j = 0; j < points.size(); j++) {
                if (j == i) continue;
                else if (points[i].x == points[j].x && points[i].y == points[j].y) samePoint++;
                else if (points[i].x == points[j].x) flag[INT_MIN]++;
                else flag [(float)(points[j].y - points[i].y) / (points[j].x - points[i].x)]++;
            }

            for (auto it = flag.begin(); it != flag.end(); ++it) {
                res = max(res, it->second + samePoint);
            }
        }

        return res;
    }
};
```
