Summary Ranges
======
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

这道题让我们做一个数组合并的算法，就是连续的数字合并起来。

解法：因为是连续的数字，我们用一个j记录连续的数字的个数，然后做缩减就好了，如果j为1的时候，就直接push结果，否则则输出压缩的结果。

```
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res;
        int i = 0;
        while (i < nums.size()) {
            int j = 1;

            while (i + j < nums.size() && nums[i + j] - nums[i] == j) j++;

            string temp = j == 1 ? to_string(nums[i]) : to_string(nums[i]) + "->" + to_string(nums[i + j - 1]);

            res.push_back(temp);
            i += j;
        }

        return res;
    }
};
```
