3Sum Closest
==============

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

这道题让我们找三个数的和最接近`target`的结果，和[3Sum](./3Sum.md)有点差不多，但是不同的地方在于，我们需要维护多一个变量，来找出这个最接近的数，我们由于我们不关注找出来的数的结果，所以我们只要维护两个变量一个是`closest`和`diff`就好了，当`diff`大于上次的`diff`则修改那两个变量就好了。

```
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int closest = nums[0] + nums[1] + nums[2], diff = abs(closest - target);
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            int temp = target - nums[i],left = i + 1, right = nums.size() - 1;
            while (left < right) {
                int thisSum = nums[left] + nums[right] + nums[i];
                int thisDiff = abs(thisSum - target);
                if (diff > thisDiff) {
                    closest = thisSum;
                    diff = thisDiff;
                }
                if (nums[left] + nums[right] > temp) right--;
                else left++;
            }
        }

        return closest;
    }
};
```

相似题目：[Two Sum](./Two Sum.md)、[3Sum](./3Sum.md)、[4Sum](./4Sum.md)
