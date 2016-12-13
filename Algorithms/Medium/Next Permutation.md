Next Permutation
=============
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

这道题的难点在于弄清楚规则究竟是什么。
例子 `[1,2,7,5,8,4,3]`
1. 从后往前找，找到第一个破坏升序的数，这里是5
1. 从后往前找，找到第一个比5大的数，这里是8
1. 5和8交换，然后再将8后面的数逆着排，这里是`[8,5,4,3]`、`[8,3,4,5]`
1. 如果整个数组是降序的，那就将数组直接升序排列就好了。


```
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int flag = -1, temp = 0;
        for (int i = nums.size() - 1; i > 0; i--) {
            if ( nums[i] > nums[i - 1]) {
                flag = i - 1;
                break;
            }
        }

        if (flag == -1) {
            sort(nums.begin(), nums.end());
            return ;
        }

        for (int i = nums.size() - 1; i > flag; i--) {
            if ( nums[i] > nums[flag] ) {
                temp = i;
                break;
            }
        }

        swap(nums[flag], nums[temp]);

        for (int i = flag + 1, j = nums.size() - 1; i <= (flag + nums.size()) / 2; i++, j--) {
            swap(nums[i], nums[j]);
        }
    }
};
```
