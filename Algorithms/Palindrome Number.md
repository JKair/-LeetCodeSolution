Palindrome Number
==================
Determine whether an integer is a palindrome. Do this without extra space.

这道题让我们判断是不是回文数，然后不能用额外的空间，意思就是让我们别想转换成string来做了

这道题的解法：用两个变量，存储要我们判断的数的左边和右边，遇到不相同则直接false。
先算这个数(x)的最高位的单位temp,x/temp则得到左边，x%10则得到右边，然后再将x的左右两边去掉，继续循环就可以了。

```
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        int temp = 1,left = 0,right = x;
        while (right >= 10) right /= 10, temp *= 10;
        while (x != 0) {
            left = x / temp;
            right = x % 10;
            if (left != right) return false;
            x %= temp;
            x /= 10;
            temp /= 100;
        }

        return true;
    }
};
```
