Reverse Integer
==============
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

这道题让我们把数字给翻转过来

我一眼望过去，就想直接强制转换字符串，然后一个一个反过来就好了，或者一个一个拿余数拼上去就好，然而这道题想考的并不是这些点，而是考如何处理溢出。
处理的方法有几种，一种是用long long型，然后判断是否过了边界，如果过了就返回0，否则返回原数值，
第二种，每次都判断绝对值的是否超过INT_MAX/10，如果超过返回0。这种做法的原因是因为，输入的数也是整型，所以第一位不可能大过2，故只要在最后一位之前先判断当前的值是否已经超过INT_MAX/10就可以了。
第三种，利用溢出后，前后的值不同的办法来判断，用一个变量存储这次的计算结果，然后除以10，看是否和上次计算结果相同，不同则直接返回0，相同则继续

这里只展示第三种解法：
```
class Solution {
public:
    int reverse(int x) {
        int res = 0,temp = res;
        while (x != 0) {
            temp = res * 10 + x%10;
            if (res != temp / 10) return 0;
            res = temp;
            x /= 10;
        }

        return res;
    }
};
```
