Jump Game
===========
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

这道题让我们判断是否可以跳过这条数组。

我们可以用动态规划来解决这道题目，递推公式是`dp[i] = max(dp[i - 1], nums[i])`，为了节省空间，我们也可以优化到只用一个变量就能解决这道问题，因为我们每次都只关心上次的结果，并不关心很久之前的结果。

```
class Solution {
public:
    bool canJump(vector<int>& nums) {
        vector<int> dp(nums.size(), 0);
        for (int i = 1; i < nums.size(); i++) {
            dp[i] = max(dp[i - 1], nums[i - 1]) - 1;
            if (dp[i] < 0) {
                return false;
            }
        }

        return dp[nums.size() - 1] >= 0;
    }
};
```

只维护一个变量：
```
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int last = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            last = max(last, nums[i]) - 1;
            if (last < 0) return false;
        }
        return last < 0 ? false:true;
    }
};
```
