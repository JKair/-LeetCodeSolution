Combinations
=============
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]


这道题让我们列出从1到n，k个数字组成的数组的全排列

解法：像这种需要遍历出所有情况的题目，我们一般使用dfs是最好解决的。

```
class Solution {
public:
    void dfs(vector<vector<int>> &res,int start, int n, int k, vector<int> &out) {
        if (out.size() == k) {
            res.push_back(out);
            return ;
        }

        for (int i = start; i <= n; i++) {
            out.push_back(i);
            dfs(res, i+1, n, k, out);
            out.pop_back();
        }
    }

    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> out;
        dfs(res, 1, n, k, out);

        return res;
    }
};
```
