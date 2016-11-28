First Missing Positive
======================

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

让我们找到缺少的数，时间复杂度和空间复杂度都必须是O(n)。

我一开始准备淫荡地排序一波解决这个问题，然而排序根本没办法满足时间复杂度，当然我自己是没想出解决办法的，然后参照了其他人的做法，其实我们只要在原数组上面修改就可以了，由于这道算法并不关心负数，所以我们遇到负数就直接跳过，当我们遇到这个数不等于当前的循环标识数`i`而且这个数不放在自己应该在的位置的时候，那么就要进行交换，例子：

[1,2,4,3,5,-1]

我们要将它变成[1,2,3,4,5,-1]，每个正数数都在自己对应的位置上，然后第二次循环的时候，跟它的位置进行比对，如果有一个数不在自己的位置上了，那么就return当前的位置

```
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        if (nums.size() == 0) return 1;
        int res[nums.size()] = {0},temp = 0;

        for (int i = 0; i < nums.size(); ) {
            if (nums[i] > 0 && nums[i] <= nums.size() && nums[i] != i + 1 && nums[i] != nums[nums[i] - 1]) {
                swap(nums[i], nums[nums[i] - 1]);
            } else {
                i++;
            }
        }

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != i + 1) return i + 1;
        }

        return nums.size() + 1;
    }
};
```
