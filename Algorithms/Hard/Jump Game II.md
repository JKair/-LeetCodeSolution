Jump Game II
==============
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
Note:
You can assume that you can always reach the last index.

这道题让我们算，最少多少部可以跳到数组完毕。我们可以认为，这一个题目是一定有解的，最后的Note里面有做说明。

解法：一开始我是直接动态规划解，然后最后是跑不过的，有一组超级大的数组，会超空间，所以只能搜索别人的解法，发现这种解法6得飞起。时间复杂度只有O(n)，空间复杂度是O(1)。[链接在这里](http://www.cnblogs.com/lichen782/p/leetcode_Jump_Game_II.html)

```
class Solution {
public:
    int jump(vector<int>& nums) {
        int last = 0, cur = 0, res = 0, n =nums.size();
        for (int i = 0; i < n; i++) {
            if (i > last) {
                last = cur;
                res++;
                if (cur >= n - 1) break;
            }
            cur = max(cur, i + nums[i]);
        }

        return res;
    }
};
```
