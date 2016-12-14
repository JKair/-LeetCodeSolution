Triangle
=======
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

这道题给出三角形，让我们找出从三角形顶一直跑到底的最小权值。

解法：这道题要求我们保持空间复杂度为O(n)，实际上我们在计算的过程中，只需要直接使用给予的二维数组来更新就可以了，递推公式为`triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])`，再就是处理边界值的问题就可以了。

```
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                if (j == 0) triangle[i][j] += triangle[i-1][j];
                else if (j == i) triangle[i][j] += triangle[i-1][j-1];
                else triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1]);
            }
        }
        int res = triangle[n-1][0];

        for (int i = 0; i < triangle[n - 1].size(); i++) {
            res = min(triangle[n - 1][i], res);
        }

        return res;
    }
};
```
