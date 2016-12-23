Two Sum II - Input array is sorted
============
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

这道题让我们在一个有序的数组里面找到两个值等于`target`的情况，只需要找到一种，所以就算有重复也不用理。

解法：这道题我们只要用两个指针，一个从前往后，一个从后往前，这样向中间扫就可以了，当遇到大于`target`的时候，就后面的往前，否则则相反。

```
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0,right = numbers.size() - 1;
        while (left <= right) {
            if (target == numbers[left] + numbers[right]) {
                return {left+1, right+1};
            } else if (target > numbers[left] + numbers[right]) {
                left++;
            } else {
                right--;
            }
        }

        return {};
    }
};
```

相似题目[Two Sum](../Easy/Two Sum.md)
