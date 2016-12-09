Subsets II
===========
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

这道题和[Subsets](./Subsets.md)的不同之处在于，我们需要处理重复值的情况。

解法：我们在`Subsets`的变化过程上，我们可以发现，问题出在遇到相同数字的时候，当我们跑完第一个2的时候，结果是`[[],[1],[2],[1,2]]`，第二个2的时候，我们不能在尾部插入`[[],[1],[2],[1,2]]`，并添加2上去，我们要插入的是`[[2],[1,2]]`，也就是插入`1`的时候的数组长度了。这样问题就解开了。

```
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> res(1);
        sort(nums.begin(), nums.end());
        int last = nums[0], lastSize = 1;
        for (int i = 0; i < nums.size(); i++) {
            if (last != nums[i]) {
                last = nums[i];
                lastSize = res.size();
            }
            int size = res.size();
            for (int j = size - lastSize; j < size; j++) {
                res.push_back(res[j]);
                res.back().push_back(nums[i]);
            }
        }

        return res;
    }
};
```

相似题目[Subsets](./Subsets.md)
