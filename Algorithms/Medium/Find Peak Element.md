Find Peak Element
============
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.

这道题让我们找峰。但是注意，并不是让我们找最高峰，就算是局部最高峰也是可以的。

解法：其实我觉得这道题设计的并不是太好，因为只要找局部最高峰就好了，所以我们只要知道什么时候出现了递减数列，则可以知道此处必是局部高峰。

```
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] < nums[i - 1]) return i - 1;
        }
        return nums.size() - 1;
    }
};
```
