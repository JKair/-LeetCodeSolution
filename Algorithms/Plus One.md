Plus One
=========
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.


这道题让我们给数组的数字+1。

实际上这道题定位为Easy大概是因为测试样例的问题吧，因为只需要考虑自然数的情况，不需要考虑小数，正负数那些所以才变得如此简单，我们从高位遍历到低位，只需要处理为9的情况，当为9的时候，则变为0，当加的时候不为0，则可以直接退出，如果遍历到最低位，还是9，变为0后，再在最低位插入1就可以了。

```
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i = digits.size()-1; i >= 0 ; i--) {
            if (digits[i] == 9) digits[i] = 0;
            else {
                digits[i]++;
                return digits;
            }
        }
        if (digits[0] == 0) digits.insert(digits.begin(), 1);

        return digits;
    }
};
```
