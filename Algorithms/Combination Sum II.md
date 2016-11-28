Combination Sum II
===================

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

这道题实际上和`Combination Sum`类似，只是变成每个数字只能使用一次。

套路基本上和`Combination Sum`差不多，还是递归dfs思想，但是为了去重，我们可以直接把vector换成set，因为set的特性，就可以直接去重了。

```
class Solution {
public:
    void combinationSum2(vector<int> &nums, vector<int> &out, set<vector<int>> &res, int target, int start) {
        if (target == 0) {
            res.insert(out);

            return ;
        }

        for (int i = start; i < nums.size(); i++) {
            if (nums[i] > target) break;
            out.push_back(nums[i]);
            combinationSum2(nums,out,res,target-nums[i], i+1);
            out.pop_back();
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> out;
        set<vector<int>> res;
        combinationSum2(candidates, out, res, target, 0);

        vector<vector<int>> last(res.begin(), res.end());

        return last;
    }
};
```


相似题目[Combination Sum](./Combination Sum.md)
