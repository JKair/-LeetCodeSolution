Combination Sum

Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]

这道题让我们找出在一个数组里面，所有的target的解。

感觉这种题目的套路都差不多，由于解的个数不定，所以我们只要递归进去就好了，dfs的思想，套路都差不多。

```
class Solution {
public:
    void combinationSum(vector<int> &nums, vector<int> &out, vector<vector<int>> &res, int target, int start) {
        if (target == 0) {
            res.push_back(out);

            return ;
        }

        for (int i = start; i < nums.size(); i++) {
            if (nums[i] > target) break;
            out.push_back(nums[i]);
            combinationSum(nums,out,res,target-nums[i], i);
            out.pop_back();
        }
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> out;
        vector<vector<int>> res;
        combinationSum(candidates, out, res, target, 0);

        return res;
    }
};
```

相似题目[Combination Sum II](./Combination Sum II.md)、[Combination Sum III](./Combination Sum III.md)
