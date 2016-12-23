Largest Number
====
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

这道题让我们用数字里面所有的数字拼凑出最大的数字

解法：我们要对所有的数进行排序，排序的条件是`ab > ba`，因为我们只要将前后两个数组合，就知道这样组合能不能组合出最大数了，然后推到多个数的情况，只要将整个数组的数都排序一边，最后拼凑则可以得出结果。

```
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end(), [](int &i, int &j){
            return to_string(i)+to_string(j)>to_string(j)+to_string(i);
        });

        string res;

        for (auto i : nums) res += to_string(i);
        while (res[0] == '0' && res.size() > 1) res.erase(0, 1);
        return res;
    }
};
```
