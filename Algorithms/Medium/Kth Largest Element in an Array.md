Kth Largest Element in an Array
========
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

这道题让我们找一个数组里面第k大的数。

解法：我们可以利用小顶堆去解决这个问题，小顶堆里面最多只有k个数字，如果超过就去除最尾部的数字。

```
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int,vector<int>, greater<int>> res;
        for (int i = 0; i < nums.size(); i++) {
            res.push(nums[i]);
            if (res.size() > k) {
                res.pop();
            }
        }

        return res.top();
    }
};
```
