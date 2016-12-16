Single Number II
=======
Given an array of integers, every element appears three times except for one. Find that single one.

这道题和`Single Number`差不多，但是不同的地方在于，这次是出现三次了。

解法一：比较直的思路，我们可以先用数组排序一下，然后比对三个连续的值，如果出现不同就在这里面返回，如果循环数到了最后一个，那么最后一个一定就是那个数了。

```
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int i = 0;
        while (i < nums.size() - 1) {
            if (nums[i] == nums[i + 1] && nums[i] == nums[i + 2]) i += 3;
            else return nums[i] ^ nums[i + 1] ^ nums[i + 2];
        }

        return nums[i];
    }
};
```

解法二：第二种解法比较晦涩一点，需要理解位运算的与操作还有取反，我们需要知道`~`操作是把所有的位都取一个相反数，任何数和1进行与运算都等于他本身，而任何数和他的反数进行与运算都等于0，于是我们可以推出递推式。= =自己细细品味，我自己也很难描述那种味道。

```
ones = (ones ^ A[i]) & ~twos;
twos = (twos ^ A[i]) & ~ones;
```

```
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ones = 0, twos = 0;
        for(int i = 0; i < nums.size(); i++){
            ones = (ones ^ nums[i]) & ~twos;
            twos = (twos ^ nums[i]) & ~ones;
        }
        return ones;
    }
};
```


相似题目[Single Number](../Easy/Single Number.md)
