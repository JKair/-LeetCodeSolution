Spiral Matrix
================

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].


这个题目让我们以一个画圆圈的形式来输出一个矩阵。

解法：这道题我们有四个任务要处理，就是往右边跑，往下跑，往左边跑，往上面跑，而且每个任务后面还要缩小矩形，重复上述流程。这道题难度在于如何处理边界的问题。我们其实可以用四个变量来表示边界，上下左右，`然后跑第一个任务，跑完之后缩小上边界，如果发现上边界已经越过下边界了，那么直接退出`，然后第二个任务，第三个任务，第四个，这样最后就能得到结果了。

```
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.empty()) return {};
        int i = 0,top = 0,bot = matrix.size() - 1,left = 0,right = matrix[0].size() - 1;
        vector<int> res;
        while (top <= bot || left <= right) {
            //往右边跑
            i = left;
            while (i <= right) {
                res.push_back(matrix[top][i++]);
            }
            if (++top > bot) break;
            //往下跑
            i = top;
            while (i <= bot) {
                res.push_back(matrix[i++][right]);
            }
            if (--right < left) break;
            //往左跑
            i = right;
            while (i >= left) {
                res.push_back(matrix[bot][i--]);
            }
            if (--bot < top) break;
            //往上跑
            i = bot;
            while (i >= top) {
                res.push_back(matrix[i--][left]);
            }
            if (++left > right) break;
        }

        return res;
    }
};
```
