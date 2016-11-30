Maximum Subarray
===========
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

这道题让我们找出最大的连续子序列的和，时间复杂度要求O(n)

其实这道题的思路挺多的，一开始我的思路是动态规划，用一个二维数组去记录每次的值，然后筛选到最大的值，然后二维数组最后会超空间，之后，发现其实用一维数组也完全可以解决，然后就用一维数组去记录，再后来发现，实际上，我们遍历一次数组，遍历到每一位上，我们都是要求当前位置的最大值，所以我们只需要求`max(last, last+nums[i])`。

```
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int last = nums[0],res = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            last = max(nums[i], last + nums[i]);
            res = max(last, res);
        }

        return res;
    }
};
```
