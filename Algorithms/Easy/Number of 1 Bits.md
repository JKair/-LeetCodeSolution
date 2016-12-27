Number of 1 Bits
========
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

这道题让我们数数的二进制里面有多少个1。

解法：这道题考验我们位操作，我们用与操作，取最低位，然后一位一位识别就好了。

```
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int res = 0;

        for (int i = 0; i < 32; i++) {
            res += (n & 1);
            n >>= 1;
        }

        return res;
    }
};
```
