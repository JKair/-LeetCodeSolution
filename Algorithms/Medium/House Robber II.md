House Robber II
======
After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

这道题是`House Robber`的扩展，将所有的房子变成了一个圆圈。

解法：其实解题的思路基本一样，但是我们要修改一个地方，就是由于房子编程圆圈了，所以房子，你偷了第一间就不能偷最后一间了，所以实际上，我们只要将这个圆给拆开，分别计算去掉第一个节点和最后一个节点的情况，就可以解决问题了。

```
class Solution {
public:
    int rob(vector<int>& nums, int left, int right) {
        int dan = 0,shuang = 0;
        for (int i = left; i < right; i++) {
            if (i%2 == 0) {
                shuang += nums[i];
                shuang = max(dan,shuang);
            } else {
                dan += nums[i];
                dan = max(dan,shuang);
            }
        }

        return max(dan,shuang);
    }
    int rob(vector<int>& nums) {
        if (nums.size() <= 1) return nums.empty() ? 0 : nums[0];
        return max(rob(nums,0,nums.size()-1), rob(nums, 1, nums.size()));
    }
};
```

相似题目[House Robber](../Easy/House Robber.md)
