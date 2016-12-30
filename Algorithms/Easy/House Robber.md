House Robber
=========
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

这道题是说，假设你是一个小偷，你要偷钱，给你一系列连续的房子，每个房子有的价值就那么多，你不能连续偷两家，不然就会启动报警系统，问你最多偷到多少钱。

解法一：这道题是典型的动态规划题目，感觉上是和爬楼梯有异曲同工之妙啊，递推式是`temp = max(res[i - 2] + nums[i], res[i - 1]);`

```
class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        } else if (nums.size() == 1) {
            return nums[0];
        }
        vector<int> res;
        res.push_back(nums[0]);
        res.push_back(max(nums[0],nums[1]));
        int temp = res[0];
        for (int i = 2; i < nums.size(); i++) {
            temp = max(res[i - 2] + nums[i], res[i - 1]);

            res.push_back(temp);
        }

        return res[res.size()-1];
    }
};
```

解法二：由于只是限定了不能连续，所以其实我们可以把房子分成单双来算，把空间优化到O(1)

```
class Solution {
public:
    int rob(vector<int>& nums) {
        int dan = 0,shuang = 0;
        for (int i = 0; i < nums.size(); i++) {
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
};
```

相似题目[House Robber II](../Medium/House Robber II.md)
