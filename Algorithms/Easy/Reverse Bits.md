Reverse Bits
======
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

这道题让我们将一个二进制数给翻转过来。

解法：考验我们的位操作，把每一位都拿出来，然后插进对的位置就好了。

```
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        for (int i = 0; i < 32; i++) {
            res = n & 1 ? (res << 1) + 1 : res << 1;
            n >>= 1;
        }

        return res;
    }
};
```
