Trapping Rain Water
=======
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

这道题让我们算最多能装多少雨水。

解法：首先我们可以找出最高的柱子，然后用两个指针，一个从前往后扫，一个从后往前扫，这样的话，因为柱子一定是往上升的，所以我们只要加扫描过程的最高柱子的水就好了。

```
class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty()) return 0;
        int res = 0,maxHeightIndex = 0, maxHeight = height[0];

        for (int i = 0; i < height.size(); i++) {
            maxHeightIndex = height[i] > height[maxHeightIndex] ? i : maxHeightIndex;
        }

        for (int i = 1; i < maxHeightIndex; i++) {
            if (maxHeight > height[i]) res += maxHeight - height[i];
            else maxHeight = height[i];
        }
        maxHeight = height[height.size()-1];
        for (int i = height.size() - 1; i > maxHeightIndex; i--) {
            if (maxHeight > height[i]) res += maxHeight - height[i];
            else maxHeight = height[i];
        }

        return res;
    }
};
```
