Rectangle Area
====
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
![图片](https://leetcode.com/static/images/problemset/rectangle_area.png)
Assume that the total area is never beyond the maximum possible value of int.

这道题让我们计算两个矩形的面积，矩形有可能重叠有可能包含。

解法：我们先把两个矩形的面积和算出来，然后再算重叠的部分，减去就可以了。

```
class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int res = (D - B) * (C - A) + (G - E) * (H - F);

        if (C<=E || D<=F || A>= G || B>=H)  return res;

        return res - (min(G, C) - max(A,E)) * (min(D,H) - max(B, F));
    }
};
```
