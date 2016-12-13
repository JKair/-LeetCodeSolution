Container With Most Water
=============
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

这道题会给我们一个一维数组，代表一个容器的左右柱子的大小，让我们计算两个柱子间组成的容器最多可以装多少水。

解法：我们用两个变量，分别指向左边和右边，然后向中间扫描，由于我们要计算出最大的容器面积，所以应该一直保持最大的边长，比对左右边长的时候，小的向中间靠拢。

```
class Solution {
public:
    int maxArea(vector<int>& height) {
        int start = 0, end = height.size() - 1, res = 0;

        while (start < end) {
            res = max(res, min(height[end], height[start]) * (end - start));
            if (height[start] < height[end]) start++;
            else end--;
        }

        return res;
    }
};
```
