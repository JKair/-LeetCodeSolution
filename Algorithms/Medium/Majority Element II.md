Majority Element II
=======
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

这道题让我们找出出现的次数大于n/3的数字，限定空间复杂度O(1)。

解法：这道题还是只能用摩尔投票了，这次有两个候选数字，摩尔投票可以找出出现次数最多的两个数，我们只要找到那两个数，然后多一次循环记录这两个数出现的次数，最后判断次数放进容器就好了。

```
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int cnt1 = 0, cnt2 = 0, a = 0, b = 1;
        for (int i = 0; i < nums.size(); i++) {
            if (a == nums[i]) cnt1++;
            else if (b == nums[i]) cnt2++;
            else if (cnt1 == 0) {
                cnt1++; a = nums[i];
            } else if (cnt2 == 0) {
                cnt2++; b = nums[i];
            }
            else {
                cnt1--;
                cnt2--;
            }
        }
        cnt1 = cnt2 = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (a == nums[i]) cnt1++;
            else if (b == nums[i]) cnt2++;
        }

        vector<int> res;
        if (cnt1 > nums.size() / 3) res.push_back(a);
        if (cnt2 > nums.size() / 3) res.push_back(b);

        return res;
    }
};
```

相似题目[Majority Element](../Easy/Majority Element.md)
