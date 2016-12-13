Permutations II
=============
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

让我们排序这个数组有可能出现的所有情况，但是必须是唯一的，和`Permutations`相比，这里我们需要判断数字是否重复了。

解法一：其实我们只需要在`Permutations`的基础上，先将数排个序，然后如果遇到前后数字相等，而且前面的数字没有遍历过的，那么就直接跳过，不遍历了。

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
            if (i > 0 && nums[i] == nums[i-1] && !flag[i-1]) continue;
            flag[i] = true;
            temp.push_back(nums[i]);
            dfs(nums, flag, temp, res, deep+1);
            temp.pop_back();
            flag[i] = false;
        }
    }

    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<int> temp;
        vector<vector<int>> res;
        vector<bool> flag(nums.size(), false);
        sort(nums.begin(), nums.end());
        dfs(nums, flag, temp, res, 0);

        return res;
    }
};
```

解法二：在`Permutations`的基础上，我们用set去去重，以及跳过和depp相同的数字则可以了。

```
class Solution {
public:
    void swapPermutations(vector<int>& nums, set<vector<int>> &res, int deep) {
        if (deep == nums.size()) res.insert(nums);
        for (int i = deep; i < nums.size(); i++) {
            if (i != deep && nums[i] == nums[deep]) continue;
            swap(nums[deep], nums[i]);
            swapPermutations(nums, res, deep+1);
            swap(nums[deep], nums[i]);
        }
    }

    vector<vector<int>> permuteUnique(vector<int>& nums) {
        set<vector<int>> res;
        swapPermutations(nums, res, 0);
        vector<vector<int>> last(res.begin(), res.end());
        return last;
    }
};
```


相似题目：[Permutations](./Permutations.md)
