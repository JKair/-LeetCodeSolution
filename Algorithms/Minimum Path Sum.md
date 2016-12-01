Minimum Path Sum
=================
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.


这道题让我们计算最小的路径和。

这道题实际上是最常规的dp题目了。

```
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int res[m][n];
        res[0][0] = grid[0][0];
        for (int i = 1; i < m; i++) res[i][0] = res[i-1][0] + grid[i][0];
        for (int i = 1; i < n; i++) res[0][i] = res[0][i-1] + grid[0][i];
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                res[i][j] = grid[i][j] + min(res[i-1][j], res[i][j-1]);
            }
        }

        return res[m-1][n-1];
    }
};
```
