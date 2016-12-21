Maximum Product Subarray
==========
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

这道题让我们算一下连续的版本号最大的乘积。

解法一：动态规划，这种题很容易让人想到动态规划去解决，因为思路比较直接，但是时间复杂度是O(n²)，OJ最后一组1.5W的大数过不了。所以这个方法还是要去优化。

```
Status: Time Limit Exceeded

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.empty()) return 0;
        int n = nums.size(), res = nums[0];
        vector<vector<int>> temp(n, vector<int>(n, 1));
        temp[0][0] = nums[0];

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                temp[i][j] = j == i ? nums[j] : temp[i][j - 1] * nums[j];
                res = max(res, temp[i][j]);
            }
        }

        return res;
    }
};
```

解法二：重新做流程的优化，其实我们难处理的问题在于负数，我们需要记录每次到当前节点的最大值和最小值就好了，当遇到负数的时候，肯定是从第一个累计过来的最小值乘以负数得到的最大值是最大的，然后正数的时候，我们则需要衡量要不要放弃前面所有的版本了，也就是比较1和当前记录的最大值谁大，得出后相乘得到结果。

```
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int maxPro = 1, min = 1, res = nums[0];

        for (int i = 0; i < nums.size(); i++) {
            int oldMax = max(maxPro, 1);
            if (nums[i] > 0) {
                maxPro = oldMax * nums[i];
                min *= nums[i];
            } else {
                maxPro = min * nums[i];
                min = oldMax * nums[i];
            }

            res = max(res, maxPro);
        }

        return res;
    }
};
```
