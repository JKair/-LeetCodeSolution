Factorial Trailing Zeroes
========
Given an integer n, return the number of trailing zeroes in n!.

让我们求n的阶乘里面，0的个数。

解法：其实这道题就是转换成乘以了多少个10，由于10可以分解成2*5，2的话每两个数出现一次，5则每5个数出现一次，所以2肯定比5多，那么我们只要数5的个数就好了。

```
class Solution {
public:
    int trailingZeroes(int n) {
        int res = 0;
        while (n) {
            n /= 5;
            res += n;
        }

        return res;
    }
};
```
