Minimum Size Subarray Sum
========
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

这道题让我们查找可以让和等于`s`的最小的连续数列的个数。

解法：我们可以用一像窗口一样的算法，用两个指针一个是left，一个right，分别表示这个窗口的左右边界。在这个窗口里面的数，如果可以满足要求，那么就计算这个窗口的长度，然后接下来缩短左边界，让右边界继续往右边走，直到right结束。

```
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        if (nums.empty()) return 0;
        int left = 0, right = 0, len = nums.size(), res = len + 1, sum = 0;

        while (right < len) {
            while (sum < s && right < len) {
                sum += nums[right++];
            }

            while (sum >= s && left <right) {
                res = min(res, right-left);
                sum -= nums[left++];
            }
        }

        return res == len + 1 ? 0 : res;
    }
};
```
