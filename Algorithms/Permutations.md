Permutations
=============
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

列出给定数组的数的所有排列情况。

感觉这道题的套路和之前[Combination Sum](./Combination Sum.md)差不多，都是用dfs解决，然而这道题要变通一下，需要多一个数组去记录当前的数字有没有使用过。

```
class Solution {
public:
    void dfs(vector<int>& nums, vector<bool> &flag, vector<int> &temp, vector<vector<int>> &res, int deep) {
        if (deep == nums.size()) {
            res.push_back(temp);

            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (flag[i]) continue;
            temp.push_back(nums[i]);
            flag[i] = true;
            dfs(nums, flag, temp, res, deep+1);
            temp.pop_back();
            flag[i] = false;
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> temp;
        vector<vector<int>> res;
        vector<bool> flag(nums.size(), false);
        dfs(nums, flag, temp, res, 0);

        return res;
    }
};
```
