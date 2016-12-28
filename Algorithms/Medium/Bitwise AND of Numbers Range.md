Bitwise AND of Numbers Range
========
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

这道题让我们找数字范围内位相与。

解法：其实我一直没看明白题目的意思，最后还是找了别人的解法。按照这个[论坛](https://discuss.leetcode.com/topic/12111/accepted-c-solution-with-simple-explanation)的说法，就是`等价于 求 m 与 n 二进制编码中 的共同前缀`。如果是这样的话，求前缀最好的做法，就是将m和n都一直右移，直到两个数都相等，最后再左移就好了。

```
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        int i = 0;
        while (m != n) {
            m >>= 1, n >>= 1;
            i++;
        }

        return m << i;
    }
};
```
